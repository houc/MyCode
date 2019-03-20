import unittest
import os

from model.ExcelReport import ExcelTitle
from model.Yaml import MyYaml
from model.SQL import Mysql
from model.MyException import SQLDataError, FUN_NAME
from model.SendEmail import Email
from model.CaseHandle import data_handle


class RunAll(object):
    def __init__(self):
        """初始化"""
        self.current_path = os.path.dirname(__file__)
        self.re = MyYaml('re').config
        self.sql = Mysql()
        self.wait = MyYaml('while_sleep').config
        self.case = MyYaml('while_case').config
        self.excel = ExcelTitle

    def _clear_sql(self):
        """清除数据库所有的内容"""
        self.sql.delete_data()

    def _running(self):
        """所有以_st.py作为需运行的py"""
        self._clear_sql()
        module_run = MyYaml('module_run').config
        project_name = MyYaml('project_name').excel_parameter
        if module_run is not None:
            self.current_path = self.current_path + '/{}/{}'.format(project_name, module_run)
        discover = unittest.defaultTestLoader.discover(self.current_path, self.re)
        runners = unittest.TextTestRunner()
        result = runners.run(discover)
        return result

    def run(self):
        """测试用例数据处理，并执行用例"""
        run = self._running()
        sql_query = self.sql.query_data()
        result = data_handle(data=sql_query, case=run)
        if sql_query:
            self.excel(sql_query).class_merge(parameter=result)
            self._send_email()
        else:
            raise SQLDataError(FUN_NAME(self.current_path))

    def _send_email(self):
        """发送邮件"""
        Email().sender_email()


if __name__ == '__main__':
    T = RunAll()
    T.run()
