import unittest
import os

from model.ExcelReport import ExcelTitle
from model.Yaml import MyYaml
from model.MyDB import MyDB
from model.SendEmail import Email
from model.CaseHandle import DataHandleConversion, ConversionDiscover
from model.TimeConversion import standard_time


class RunAll(object):
    def __init__(self):
        """初始化"""
        self.current_path = os.path.dirname(__file__)
        self.re = MyYaml('re').config
        self.sql = MyDB(switch=False)
        self.mail = Email()
        self.start_time = standard_time()
        self.wait = MyYaml('while_sleep').config
        self.case = MyYaml('while_case').config
        self.thread = MyYaml('thread').config
        self.excel = ExcelTitle
        self.handle_data = DataHandleConversion
        self._clear_sql()

    def _clear_sql(self):
        """清除数据库所有的内容"""
        self.sql.delete_data()

    def _get_execute_case(self):
        """获取需要执行的路径"""
        module_run = MyYaml('module_run').config
        project_name = MyYaml('project_name').excel_parameter
        if module_run is not None:
            self.current_path = self.current_path + '/{}/{}'.format(project_name, module_run)
        discover = unittest.defaultTestLoader.discover(self.current_path, self.re)
        if self.thread:
            ConversionDiscover(discover)
        else:
            runner = unittest.TextTestRunner(verbosity=2)


    def run(self):
        """测试用例数据处理，并执行用例"""





if __name__ == '__main__':
    runner = RunAll()
    runner.run()