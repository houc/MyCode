import unittest
import os
import asyncio

from model.ExcelReport import ExcelTitle
from model.Yaml import MyYaml
from model.SQL import Mysql
from model.SendEmail import Email
from model.CaseHandle import DataHandleConversion


class RunAll(object):
    def __init__(self):
        """初始化"""
        self.current_path = os.path.dirname(__file__)
        self.re = MyYaml('re').config
        self.sql = Mysql()
        self.wait = MyYaml('while_sleep').config
        self.case = MyYaml('while_case').config
        self.excel = ExcelTitle
        self.handle_data = DataHandleConversion

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

    @asyncio.coroutine
    async def run(self):
        """测试用例数据处理，并执行用例"""
        run = self._running()
        self._case_data(case_data=run)
        sql_query = self.sql.query_data()
        result = self._sql_data(sql_data=sql_query)
        if sql_query:
            self.excel(sql_query).class_merge(parameter=result)
            self._send_email()
            self.sql.close_sql()

    def _send_email(self):
        """发送邮件"""
        Email().sender_email()

    def _case_data(self, case_data=None):
        """
        数据处理中心
        :param case_data: 处理self._running中的用例数据
        :param sql_data:
        :return 返回处理后的数据
        """
        self.handle_data(case_data=case_data).case_data_handle()

    def _sql_data(self, sql_data=None):
        """

        :param sql_data: 处理sql查询出来的数据，主要用于excel表总况的统计处理数据
        :return: 返回处理后的数据
        """
        return self.handle_data(sql_data=sql_data).sql_data_handle()



if __name__ == '__main__':
    runner = RunAll()
    pool = asyncio.get_event_loop()
    pool.run_until_complete(runner.run())
    pool.close()