import unittest
import os

from model.ExcelReport import ExcelTitle
from model.Yaml import MyYaml
from model.SQL import Mysql
from model.MyException import SQLDataError, FUN_NAME
from model.SendEmail import Email


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
        result = self._sqlAndCase_data_handle(case=run, data=sql_query)
        if sql_query:
            self.excel(sql_query).class_merge(parameter=result)
            self._send_email()
        else:
            raise SQLDataError(FUN_NAME(self.current_path))


    def _send_email(self):
        """发送邮件"""
        Email().sender_email()

    def _sqlAndCase_data_handle(self, data=None, case=None):
        """
        :param case: 传入用例的所有信息，提取总用例数、错误数、失败数、成功数
        :param data: 传入从数据库中查询出来的结果后提取开始时间、结束时间、用例最短最短耗时，用例最长耗时
        :return: 列表的形式进行返回对应数据【开始时间、结束时间、用例最短最短耗时，用例最长耗时，总用例数、错误数、失败数、成功数】
        """
        case_messages = {}
        sql_data = []
        member = []
        # =======================================处理数据库中的数据============================================

        if data is not None:
            for first_data in range(len(data)):
                _data = data[first_data]
                for second_data in range(len(_data)):
                    if first_data == 0:
                        if second_data == 12:
                            case_messages["start_time"] = _data[second_data]
                    if second_data == 9:
                        sql_data.append(float(_data[second_data][:-1]))
                    if second_data == 11:
                        member.append(_data[second_data])
                    if first_data == len(data) - 1:
                        if second_data == 12:
                            case_messages["end_time"] = _data[second_data]
            if sql_data and member:
                case_messages["short_time"] = min(sql_data)
                case_messages["long_time"] = max(sql_data)
                case_messages["member"] = list(set(member))

        # =======================================处理用例统计数据=============================================

        if case is not None:
            case_messages["testsRun"] = case.testsRun
            case_messages["errors"] = len(case.errors)
            case_messages["failures"] = len(case.failures)
            case_messages["success"] = case.testsRun - (len(case.errors) + len(case.failures))
        if case_messages:
            return case_messages



if __name__ == '__main__':
    T = RunAll()
    T.run()