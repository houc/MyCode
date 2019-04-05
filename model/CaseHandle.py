import os
import time
import warnings
import unittest

from threading import Thread
from multiprocessing import Pool, Process
from model.Yaml import MyYaml
from model.MyException import SQLDataError, FUN_NAME
from model.TimeConversion import beijing_time_conversion_unix, time_conversion, standard_time
from config_path.path_file import read_file
from model.MyDB import MyDB


class DataHandleConversion(object):
    def __init__(self):
        self.sql = MyDB(switch=False)
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
            start_time = beijing_time_conversion_unix(case_messages['start_time'])
            ends_time = beijing_time_conversion_unix(case_messages['end_time'])
            case_messages['total_time'] = time_conversion(ends_time - start_time)
            if case_messages:
                return case_messages
        else:
            raise SQLDataError(FUN_NAME(self.current_path))

    def case_data_handle(self, in_case_data):
        """用例数据处理"""
        global module, is_case, da
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
                        skipped.append({"module": module, "case_name": is_case,
                                        "reason": "跳过原因: {}".format(skip),
                                        "insert_time": standard_time()})
            self._insert_case_data(data=skipped)
        else:
            warnings.warn('self.case_data is None')

    def _insert_case_data(self, data):
        """用例数据插入sql"""
        if data:
            for is_data in data:
                self.sql.insert_data(id=None, level=None, module=is_data["module"], name=is_data["case_name"],
                                     remark=None, wait_time=None, status="跳过", url=None,
                                     insert_time=is_data["insert_time"], img=None, error_reason=is_data["reason"],
                                     author=None, results_value=None)


class ConversionDiscover(object):
    def __init__(self, discover, encoding='utf8'):
        self.discover = discover
        self.encoding = encoding
        self.project = MyYaml('project_name').excel_parameter
        self.module = MyYaml('module_run').config
        self.case_handle = DataHandleConversion()
        self._execute_discover()

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
            content = {'\n\n__all__ = [%s]' % str(set(class_name)).replace('{', '').replace('}', '').
                replace("'", "").replace(',', ', \n')}
            return self._write_execute_module(set(module), content)
        else:
            raise ValueError('The test suite is empty')

    def _write_execute_module(self, module, class_name):
        """写入需要执行的模块"""
        write_path = read_file(self.project, '__init__.py')
        with open(write_path, 'wt', encoding=self.encoding) as f:
            f.writelines(module)
        with open(write_path, 'at', encoding=self.encoding) as f:
            f.writelines(class_name)
        # self._execute_class_name()
        Process(target=self.test).start()

    def test(self):
        print(5555)

    # def _execute_class_name(self):
    #     """执行多线程或者是多进程运行测试用例以className方式进行执行操作"""
        # from Manufacture import __all__
        # for process in __all__:
        #     discover = unittest.defaultTestLoader.loadTestsFromTestCase(process)
            # result = unittest.TextTestRunner(verbosity=2).run(discover)
            # print(result)
        # for process in __all__:
        #     run = _process(process)
        #     run.start()


# class _process(Process):
#     def __init__(self, class_name):
#         Process.__init__(self)
#         self.class_name = class_name
#
#     def run(self):
#         discover = unittest.defaultTestLoader.loadTestsFromTestCase(self.class_name)
#         result = unittest.TextTestRunner(verbosity=2).run(discover)
#         print(self.)