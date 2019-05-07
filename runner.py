import unittest
import os

from model.ExcelReport import ExcelTitle
from model.Yaml import MyConfig
from model.SQL import Mysql
from model.MyDB import MyDB
from model.SendEmail import Email
from model.CaseHandle import DataHandleConversion, ConversionDiscover
from model.TimeConversion import standard_time
from config_path.path_file import read_file


class RunAll(object):
    def __init__(self, encoding='utf8'):
        """初始化"""
        self.current_path = os.path.dirname(__file__)
        self.re = MyConfig('re').config
        sql_type = MyConfig('execute_type').sql
        if 'my_sql' == sql_type:
            self.sql = Mysql()
        else:
            self.sql = MyDB()
        project = MyConfig('project_name').excel_parameter
        path = read_file(project, 'case.txt')
        with open(path, 'wt', encoding=encoding):
            pass
        self.mail = Email()
        self.start_time = standard_time()
        self.wait = MyConfig('while_sleep').config
        self.case = MyConfig('while_case').config
        self.thread = MyConfig('thread').config
        self.excel = ExcelTitle
        self._clear_sql()

    def _clear_sql(self):
        """清除数据库所有的内容"""
        self.sql.delete_data()

    def _get_case_status(self):
        """获取需要执行的路径，并执行用例"""
        module_run = MyConfig('module_run').config
        project_name = MyConfig('project_name').excel_parameter
        if module_run is not None:
            self.current_path = self.current_path + '/{}/{}'.format(project_name, module_run)
        discover = unittest.defaultTestLoader.discover(self.current_path, self.re)
        if self.thread:
            ConversionDiscover(discover).case_package()
        else:
            runner = unittest.TextTestRunner(verbosity=2).run(discover)
            DataHandleConversion().case_data_handle(in_case_data=runner)
            self._get_case_detailed()

    def _get_case_detailed(self):
        """获取需要执行的用例并运行对应的用例"""
        case_data = self.sql.query_data()
        total_case = DataHandleConversion().sql_data_handle(in_sql_data=case_data,
                                                            start_time=self.start_time,
                                                            end_time=standard_time())
        if total_case and case_data:
            self.excel(case_data).class_merge(parameter=total_case)
            self.mail.sender_email(case_name=total_case)
        else:
            import sys
            print('测试用例数据为空，无测试报告统计，无邮件...', file=sys.stderr)

    def runner(self):
        """运行全部的测试用例数"""
        self._get_case_status()


if __name__ == '__main__':
    RunAll().runner()

