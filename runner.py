import unittest
import os
import sys

from model.HtmlDataHandle import MyReport
from model.Yaml import MyConfig
from model.SQL import Mysql
from model.MyDB import MyDB
from model.SendEmail import Email
from model.CaseHandle import DataHandleConversion, ConversionDiscover
from model.TimeConversion import standard_time
from config_path.path_file import read_file
from model.ExcelReport import ExcelTitle


class RunAll(object):
    def __init__(self, encoding='utf8'):
        """初始化"""
        self.current_path = os.path.dirname(__file__)
        self.re = MyConfig('re').config
        self.save = MyConfig('save').report
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
            ExcelTitle(case_data).class_merge(total_case)
            report = MyReport().execute(case_data, start_time=total_case['start_time'],
                               ends_time=total_case['end_time'], short_time=total_case['short_time'],
                               long_time=total_case['long_time'], total_case=total_case['testsRun'],
                               error_case=total_case['errors'], failed_case=total_case['failures'],
                               success_case=total_case['success'], skipped_case=total_case['skipped'],
                               execute_time=total_case['total_time'], execute_method='单线程',
                               efficiency=total_case['efficiency'], version=total_case['version'],
                               tool=total_case['tool'], science=total_case['science'], project=total_case['project'],
                               sort_time=total_case['short_time'], fraction=total_case['fraction'])
            print('HTML测试报告已生成，访问url', report, file=sys.stderr)
            self.mail.sender_email(url=report, case_name=total_case)

    def runner(self):
        """运行全部的测试用例数"""
        if self.save < 7:
            raise ValueError('报告存放日期需大于7天以上！')
        self._get_case_status()


if __name__ == '__main__':
    RunAll().runner()

