import unittest
import os

from model.Yaml import MyConfig
from model.MyDB import MyDB
from model.SendEmail import Email
from model.CaseHandle import ConversionDiscover as excute
from model.TimeConversion import standard_time
from model.CaseSupport import TestRunning


class RunAll(object):
    def __init__(self):
        """初始化"""
        self.current_path = os.path.dirname(__file__)
        self.re = MyConfig('re').config
        self.save = MyConfig('save').report
        self.mail = Email()
        self.start_time = standard_time()
        self.thread = MyConfig('thread').config
        self.re_run_count = MyConfig('re_run_count').config
        self._clear_sql()

    def _clear_sql(self):
        """清除数据库所有的内容"""
        MyDB().delete_data()

    def _get_case_status(self):
        """获取需要执行的路径，并执行用例"""
        module_run = MyConfig('module_run').config
        project_name = MyConfig('project_name').excel_parameter
        if module_run is not None:
            self.current_path = self.current_path + '/{}/{}'.format(project_name, module_run)
        discover = unittest.defaultTestLoader.discover(self.current_path, self.re)
        if self.thread:
            thread = excute(discover=discover, start_time=self.start_time, thread_count=8)
            thread.case_package()
        else:
            runner = TestRunning()
            runner.run(discover)
            finish = excute(start_time=self.start_time, discover=None)
            finish.get_case_detailed()

    def runner(self):
        """运行全部的测试用例数"""
        if self.save < 7:
            raise ValueError('报告存放日期需大于7！')
        if self.thread and self.re_run_count > 1:
            raise ValueError('当线程启用时，重跑次数需大于1！')
        self._get_case_status()


if __name__ == '__main__':
    RunAll().runner()
