import os
import sys
import platform
import threading
import dataclasses
import selenium

from model.Yaml import MyConfig
from model.SendEmail import Email
from datetime import datetime
from model.MyException import SQLDataError, FUN_NAME
from model.TimeConversion import beijing_time_conversion_unix, time_conversion, standard_time
from model.MyDB import MyDB
from model.HtmlDataHandle import MyReport
from . HtmlReport import IP, PORT
from model.ExcelReport import ExcelTitle
from model.CaseSupport import TestRunning


class DataHandleConversion(object):
    def __init__(self, encoding='utf8'):
        self.project_name = MyConfig('project_name').excel_parameter
        self.version = MyConfig('test_version').excel_parameter
        self.science = MyConfig('science').excel_parameter
        self.encoding = encoding
        self.current_path = os.path.dirname(__file__)

    def sql_data_handle(self, in_sql_data, start_time, end_time):
        """
        通过数据库的结果进行查询统计
        :param in_sql_data: 数据库全部的信息
        :param start_time: 开始执行的时间，此处的时间为标准的北京时间
        :param end_time: 结束时间，此处的时间为标准的北京的时间
        :return: 返回对应统计结果
        """
        case_messages = {}  # 封装进行集体打包
        sql_data = []  # 用例执行的时间
        member = []  # 用例负责人
        error = []  # 用例错误错
        fail = []  # 用例失败
        success = []  # 用例成功
        skip = [] # 用例跳过数
        if in_sql_data:
            for first_data in range(len(in_sql_data)):
                _data = in_sql_data[first_data]
                for second_data in range(len(_data)):
                    if first_data == 0:
                        if second_data == 12:
                            case_messages['start_time'] = start_time
                    if second_data == 6:
                        if _data[second_data] == "错误":
                            error.append(_data[second_data])
                        elif _data[second_data] == "成功":
                            success.append(_data[second_data])
                        elif _data[second_data] == "失败":
                            fail.append(_data[second_data])
                        elif _data[second_data] == "跳过":
                            skip.append(_data[second_data])
                    if second_data == 9:
                        if _data[second_data] != 'None':
                            sql_data.append(float(_data[second_data][:-1]))
                    if second_data == 11:
                        member.append(_data[second_data])
                    if first_data == len(sql_data) - 1:
                        if second_data == 12:
                            case_messages['end_time'] = end_time
            if sql_data and member:
                case_messages["short_time"] = time_conversion(min(sql_data))
                case_messages["long_time"] = time_conversion(max(sql_data))
                set_member = list(set(member))
                set_member.remove('None') if 'None' in set_member else ''
                case_messages["member"] = set_member
            else:
                case_messages["short_time"] = 0
                case_messages["long_time"] = 0
                set_member = list(set(member))
                set_member.remove('None') if 'None' in set_member else ''
                case_messages["member"] = set_member
            case_messages["testsRun"] = len(error) + len(fail) + len(success) + len(skip)
            case_messages["errors"] = len(error)
            case_messages["failures"] = len(fail)
            case_messages["success"] = len(success)
            case_messages['skipped'] = len(skip)
            if case_messages.get('end_time') is None:
                case_messages['end_time'] = end_time
            if case_messages.get('start_time') is None:
                case_messages['start_time'] = start_time
            start_time = beijing_time_conversion_unix(case_messages['start_time'])
            ends_time = beijing_time_conversion_unix(case_messages['end_time'])
            case_messages['total_time'] = time_conversion(ends_time - start_time)
            case_messages['tool'] = 'Python' + platform.python_version()
            case_messages['version'] = self.version
            total = case_messages["errors"] + case_messages["failures"] + case_messages["success"]
            try:
                efficiency = (total / case_messages['testsRun']) * 100
            except ZeroDivisionError:
                efficiency = 0
            case_messages['efficiency'] = f'{efficiency:.2f}'
            case_messages['science'] = self.science
            try:
                fraction = (len(success) / case_messages['testsRun']) * 100
            except ZeroDivisionError:
                fraction = 0
            case_messages['fraction'] = f'{fraction:.2f}'
            case_messages['project'] = self.project_name
            if case_messages:
                return case_messages
        else:
            raise SQLDataError(FUN_NAME(self.current_path))


@dataclasses.dataclass
class ConversionDiscover(object):
    discover: selenium
    start_time: datetime
    encoding: str = 'utf8'
    thread_count: int = 4

    def __post_init__(self):
        self.mail = Email()
        self.project = MyConfig('project_name').excel_parameter
        self.module = MyConfig('module_run').config
        self.case_handle = DataHandleConversion()
        self.lock = threading.Semaphore(value=self.thread_count)

    def case_package(self, queue: bool = False, verbosity: bool = True, stream=None):
        """
        获取全部要运行的测试类，并且以多线程的方式进行运行！
        :param queue: 队列方式
        :param verbosity: 是否展示详情测试过程到控制台
        :param stream: python的标准输出库
        """
        thead = []
        for case_module in self.discover:
            thead_pool = threading.Thread(target=self._threading, args=(case_module, queue,
                                                                        verbosity, stream))
            thead.append(thead_pool)
            thead_pool.start()
        for ends in thead:
            ends.join()
        self.get_case_detailed(execute_method='多线程')

    def _threading(self, suite, queue, verbosity, stream):
        """
        执行多线程运行整个项目下的测试用例集，为合理利用计算机CPU资源，采用加锁与释放锁方式实现
        :param suite: 用例集
        :param queue: 是否采用队列方式运行用例
        :param verbosity: 是否展示详情测试过程到控制台
        :param stream: python的标准输出库
        """
        self.lock.acquire()
        runner = TestRunning(sequential_execution=queue,
                             verbosity=verbosity,
                             stream=stream)
        runner.run(suite)
        self.lock.release()

    def get_case_detailed(self, execute_method='单线程'):
        """获取需要执行的用例并运行对应的用例"""
        case_data = MyDB().query_data()
        total_case = self.case_handle.sql_data_handle(in_sql_data=case_data,
                                                      start_time=self.start_time,
                                                      end_time=standard_time())
        if total_case and case_data:
            ExcelTitle(case_data).class_merge(total_case)
            report = MyReport().execute(case_data, start_time=total_case['start_time'],
                                        ends_time=total_case['end_time'], short_time=total_case['short_time'],
                                        long_time=total_case['long_time'], total_case=total_case['testsRun'],
                                        error_case=total_case['errors'], failed_case=total_case['failures'],
                                        success_case=total_case['success'], skipped_case=total_case['skipped'],
                                        execute_time=total_case['total_time'], execute_method=execute_method,
                                        efficiency=total_case['efficiency'], version=total_case['version'],
                                        tool=total_case['tool'], science=total_case['science'],
                                        project=total_case['project'], sort_time=total_case['short_time'],
                                        fraction=total_case['fraction'])
            sys.stderr.write(f'HTML测试报告已生成，可访问url在线预览报告啦: {report}\n')
            sys.stderr.flush()
            self.mail.sender_email(url=report, case_name=total_case)
