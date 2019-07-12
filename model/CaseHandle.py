import os
import sys
import warnings
import unittest
import platform

from model.Yaml import MyConfig
from model.SendEmail import Email
from model.MyException import SQLDataError, FUN_NAME
from model.TimeConversion import beijing_time_conversion_unix, time_conversion, standard_time
from config_path.path_file import read_file
from model.MyDB import MyDB
from model.HtmlDataHandle import MyReport
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
                            sql_data.append(float(_data[second_data][:-2]))
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
            case_messages['efficiency'] = '{:.2f}'.format(float((total) / case_messages["testsRun"] * 100))
            case_messages['science'] = self.science
            case_messages['fraction'] = '{:.2f}'.format(float((case_messages["errors"] + case_messages["failures"])
                                               / case_messages["testsRun"] * 100))
            case_messages['project'] = self.project_name
            if case_messages:
                return case_messages
        else:
            raise SQLDataError(FUN_NAME(self.current_path))

    def case_data_handle(self, in_case_data):
        """用例数据处理"""
        global module, is_case, da, path
        skipped = [] # 跳过用例封装的数据
        if in_case_data is not None:
            for skipp in in_case_data.skipped:
                for skip in skipp:
                    if "test_" in str(skip):
                        module = str(skip).split(' ')[-1].split('.')[-1].split(')')[0]
                        is_case = str(skip).split(' ')[0]
                        path = str(skip).split(' ')[-1].split('(')[-1].split(')')[0]
                    else:
                        if not skip:
                            skip = "None"
                        skipped.append({"module": module, "name": is_case,
                                        "reason": "跳过原因: {}".format(skip),
                                        "insert_time": standard_time(),
                                        'status': '跳过', 'id': path})
            self._insert_case_data(data=skipped)
        else:
            warnings.warn('self.case_data is None')

    @staticmethod
    def _insert_case_data(data):
        """用例数据插入skip_cast.txt"""
        if data:
            for read in data:
                MyDB().insert_data(ids=read['id'], level=None,
                                   module=read["module"], name=read["name"],
                                   remark=None, wait_time=None, status="跳过", url=None,
                                   insert_time=read["insert_time"], img=None, error_reason=read["reason"],
                                   author=None, results_value=None)


class ConversionDiscover(object):
    def __init__(self, discover=None, encoding='utf8'):
        self.discover = discover
        self.encoding = encoding
        self.project = MyConfig('project_name').excel_parameter
        self.module = MyConfig('module_run').config
        self.mail = Email()
        self.start_time = standard_time()
        self.case_handle = DataHandleConversion()

    def _execute_discover(self):
        """处理discover"""
        class_name = []
        module_import = []
        discover = str(self.discover).split(',')
        for search in discover:
            get_tests = search.split('tests=')[-1].split(' testMethod')[0].split('<')[-1]
            if '[]>' in get_tests:
                pass
            else:
                if self.module is not None:
                    if '_FailedTest' not in get_tests.split('.'):
                        import_module = 'from {}.'.format(self.project) + '{}.'.format(self.module) + \
                                        '.'.join(get_tests.split('.')[:-1]) + \
                                        ' import ' + get_tests.split('.')[-1] + '\n'
                        module_import.append(import_module)
                        class_name.append(get_tests.split('.')[-1])
                    else:
                        warnings.warn('用例中可能存在书写错误，程序已忽略该类....')
                else:
                    if '_FailedTest' in get_tests.split('.'):
                        warnings.warn('用例中可能存在书写错误，程序已忽略该类....')
                    else:
                        import_module = 'from ' + '.'.join(get_tests.split('.')[:-1]) + \
                                        ' import ' + get_tests.split('.')[-1] + '\n'
                        module_import.append(import_module)
                        class_name.append(get_tests.split('.')[-1])
        if module_import and class_name:
            content = {'\n\n__all__ = {%s}' % str(set(class_name)).replace('{', '').replace('}', '').
                replace("'", "").replace(',', ',')}
            return self._write_execute_module(set(module_import), content)
        else:
            raise ValueError('The test suite is empty')

    def _write_execute_module(self, module, class_name):
        """写入需要执行的模块"""
        write_path = read_file(self.project, 'case_set.py')
        with open(write_path, 'wt', encoding=self.encoding) as f:
            f.writelines(module)
        with open(write_path, 'at', encoding=self.encoding) as f:
            f.writelines(class_name)

    def case_package(self):
        """获取全部要运行的测试类，并且以多进程的方式进行运行！"""
        self._execute_discover()
        suite = unittest.TestSuite()
        from SCRM.case_set import __all__
        for case in __all__:
            get_suite = unittest.defaultTestLoader.loadTestsFromTestCase(case)
            suite.addTest(get_suite)
        self._threading(suite)
        self.get_case_detailed()

    def _threading(self, suite):
        runner = TestRunning(sequential_execution=True)
        runner.run(suite)

    def get_case_detailed(self):
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
                                        execute_time=total_case['total_time'], execute_method='单线程',
                                        efficiency=total_case['efficiency'], version=total_case['version'],
                                        tool=total_case['tool'], science=total_case['science'],
                                        project=total_case['project'], sort_time=total_case['short_time'],
                                        fraction=total_case['fraction'])
            sys.stderr.write(f'HTML测试报告已生成，可访问url在线预览报告啦: {report}\n')
            sys.stderr.flush()
            self.mail.sender_email(url=report, case_name=total_case)
