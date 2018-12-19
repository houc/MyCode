import unittest
import os

from model.ExcelReport import ExcelTitle
from model.Yaml import MyYaml
from model.SQL import Mysql


class RunAll:
    def __init__(self):
        """初始化"""
        self.report_excel = list()
        self.caseNames = list()
        self.current_path = os.path.dirname(__file__)
        self.re = MyYaml('re').config
        self.sql = Mysql()
        self.wait = MyYaml('while_sleep').config
        self.case = MyYaml('while_case').config

    def _clear_sql(self):
        """清除数据库所有的内容"""
        self.sql.delete_data()

    def _running(self):
        """所有以_st.py作为需运行的py"""
        self._clear_sql()
        discover = unittest.defaultTestLoader.discover(self.current_path,self.re)
        for i in str(discover).split('testMethod='):
            for j in i.split('>'):
                if 'test_' in j:
                    self.caseNames.append(j)
        runners = unittest.TextTestRunner(while_sleep = self.wait,while_case = self.case)
        result = runners.run(discover)
        return result

    def conversion(self):
        """测试用例数据处理"""
        result = self._running()
        caseTotalCount = result.testsRun
        caseSkipTotalCount = len(result.skipped)
        caseErrorTotalCount = len(result.errors)
        caseFailTotalCount = len(result.failures)
        for a in result.skipped:
            for b in a:
                print(b)

    def _send_email(self):
        """发送邮件"""



if __name__ == '__main__':
    T = RunAll()
    T.conversion()