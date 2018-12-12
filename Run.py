import unittest,os
from model.ExcelReport import ExcelTitle
from model.Yaml import MyYaml
from model.SQL import Mysql

class RunAll:
    def __init__(self):
        """初始化"""
        self.report_excel = list()
        self.current_path = os.path.dirname(__file__)
        self.re = MyYaml('re').config
        self.clear_sql = Mysql().delete_data()

    def runner(self):
        """所有以_st.py作为需运行的py"""
        caseNames = list()
        discover = unittest.defaultTestLoader.discover(self.current_path,self.re)
        for i in str(discover).split('testMethod='):
            for j in i.split('>'):
                if 'test_' in j:
                    caseNames.append(j)
        runners = unittest.TextTestRunner()
        result = runners.run(discover)
        return result,caseNames

    def case_conversion(self):
        """测试用例数据处理"""
        case = {}
        result = self.runner()
        print(result[0].skipped)
        print(result[0].testsRun, len(result[0].skipped), len(result[0].errors), len(result[0].failures, ))
        print(result[1])

    def send_email(self):
        """发送邮件"""



if __name__ == '__main__':
    T = RunAll()
    T.case_conversion()