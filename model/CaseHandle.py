import os
import sys
import warnings
import multiprocessing
import unittest
import queue

from model.Yaml import MyYaml
from model.SendEmail import Email
from model.MyException import SQLDataError, FUN_NAME
from model.TimeConversion import beijing_time_conversion_unix, time_conversion, standard_time
from config_path.path_file import read_file
from model.SQL import Mysql
from model.MyDB import MyDB
from model.ExcelReport import ExcelTitle


class DataHandleConversion(object):
    def __init__(self, encoding='utf8'):
        self.sql_type = MyYaml('execute_type').sql
        self.project_name = MyYaml('project_name').excel_parameter
        self.path = read_file(self.project_name, 'case.txt')
        self.encoding = encoding
        if 'my_sql' == self.sql_type:
            self.sql = Mysql()
        else:
            self.sql = MyDB()
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
        if in_sql_data is not None:
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
                    else:
                        if not skip:
                            skip = "None"
                        skipped.append({"module": module, "name": is_case,
                                        "reason": "跳过原因: {}".format(skip),
                                        "insert_time": standard_time(),
                                        'status': '跳过'})
            self._insert_case_data(data=skipped)
        else:
            warnings.warn('self.case_data is None')

    def _insert_case_data(self, data):
        """用例数据插入skip_cast.txt"""
        if data:
            if 'my_sql' == self.sql_type:
                for read in data:
                    self.sql.insert_data(id=None, level=None,
                                         module=read["module"], name=read["case_name"],
                                         remark=None, wait_time=None, status="跳过", url=None,
                                         insert_time=read["insert_time"], img=None, error_reason=read["reason"],
                                         author=None, results_value=None)
            else:
                with open(self.path, 'at', encoding=self.encoding) as f:
                    for case in data:
                        f.write(str(case) + '\n')


class ConversionDiscover(object):
    def __init__(self, discover, encoding='utf8'):
        self.discover = discover
        self.encoding = encoding
        self.project = MyYaml('project_name').excel_parameter
        self.module = MyYaml('module_run').config
        self.path = read_file(self.project, 'case.txt')
        sql_type = MyYaml('execute_type').sql
        self.excel = ExcelTitle
        if 'my_sql' == sql_type:
            self.sql = Mysql()
        else:
            self.sql = MyDB()
        self.queue = queue.LifoQueue()
        self.mail = Email()
        self.start_time = standard_time()
        self.case_handle = DataHandleConversion()

    def _execute_discover(self):
        """处理discover"""
        module = []
        class_name = []
        discover = str(self.discover).split(',')
        for search in discover:
            get_tests = search.split('tests')[-1].split('<')[-1].split('testMethod')[0]
            if '=[]>' in get_tests:
                pass
            else:
                if self.module is not None:
                    import_module = 'from {}.'.format(self.project) + '{}.'.format(self.module) + \
                                    '.'.join(get_tests.split('.')[:-1]) + \
                                    ' import ' + get_tests.split('.')[-1] + '\n'
                    module.append(import_module)
                    class_name.append(get_tests.split('.')[-1])
                else:
                    import_module = 'from ' + '.'.join(get_tests.split('.')[:-1]) + \
                                    ' import ' + get_tests.split('.')[-1] + '\n'
                    module.append(import_module)
                    class_name.append(get_tests.split('.')[-1])
        if module and class_name:
            content = {'\n\n__all__ = {%s}' % str(set(class_name)).replace('{', '').replace('}', '').
                replace("'", "").replace(',', ',')}
            return self._write_execute_module(set(module), content)
        else:
            raise ValueError('The test suite is empty')

    def _write_execute_module(self, module, class_name):
        """写入需要执行的模块"""
        write_path = read_file(self.project, 'thread_case.py')
        with open(write_path, 'wt', encoding=self.encoding) as f:
            f.writelines(module)
        with open(write_path, 'at', encoding=self.encoding) as f:
            f.writelines(class_name)

    def case_package(self):
        """获取全部要运行的测试类，并且以多进程的方式进行运行！"""
        thread = []
        self._execute_discover()
        from Manufacture.thread_case import __all__
        for case in __all__:
            thread.append(_my_process(case))
        for start in thread:
            start.start()
        for ends in thread:
            ends.join()
        self._handle_case()

    def _handle_case(self):
        """处理运行完成后的用例集"""
        print('多进程执行用例完成，正在生成测试报告...', file=sys.stderr)
        with open(self.path, 'rt', encoding=self.encoding) as f:
            re = f.readlines()
        if re:
            for case in re:
                self.queue.put(eval(case))
            while not self.queue.empty():
                read = self.queue.get()
                self.sql.insert_data(id=read.get('id'), level=read.get('level'),
                                     module=read.get('module'), name=read.get('name'),
                                     remark=read.get('mark'), wait_time=read.get('run_time'),
                                     status=read.get('status'), url=read.get('url'),
                                     insert_time=read.get('insert_time'), img=read.get('img_path'),
                                     error_reason=read.get('reason'), author=read.get('author'),
                                     results_value=read.get('result'))
        case_data = self.sql.query_data()
        total_case = self.case_handle.sql_data_handle(in_sql_data=case_data,
                                                      start_time=self.start_time,
                                                      end_time=standard_time())
        if total_case and case_data:
            self.excel(case_data).class_merge(parameter=total_case)
            self.mail.sender_email(case_name=total_case)


class _my_process(multiprocessing.Process):
    """自定义封装的多进程"""
    def __init__(self, case_set):
        multiprocessing.Process.__init__(self)
        self.case_set = case_set

    def run(self):
        discover = unittest.defaultTestLoader.loadTestsFromTestCase(self.case_set)
        result = unittest.TextTestRunner(verbosity=2).run(discover)
        DataHandleConversion().case_data_handle(result)
