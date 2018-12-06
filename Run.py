import unittest
from model.ExcelReport import ExcelTitle

class RunAll:
    def __init__(self):
        """初始化"""
        self.report_excel = []

    def runner(self):
        """所有以_ts.py作为需运行的py"""
        discover = unittest.defaultTestLoader.discover('./','*_st.py')
        for i in str(discover).split('testMethod='):
            for j in i.split('>'):
                if 'test_' in j:
                    self.report_excel.append(j)
        runners = unittest.TextTestRunner()
        result = runners.run(discover)
        # print(result.classNames)
        # print(result.skipped)
        # print(result.testsRun,len(result.skipped),len(result.errors),len(result.failures,))


if __name__ == '__main__':
    RunAll().runner()