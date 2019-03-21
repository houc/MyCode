import os
import time

from model.SQL import Mysql
from model.MyException import SQLDataError, FUN_NAME


class DataHandleConversion(object):
    def __init__(self, case_data=None, sql_data=None, sql_query=None):
        self.sql = Mysql()
        self.case_data = case_data
        self.sql_data = sql_data
        self.sql_query = sql_query
        self.current_path = os.path.dirname(__file__)

    def sql_data_handle(self):
        """数据库数据处理"""
        case_messages = {}  # 封装进行集体打包
        sql_data = []  # 用例执行的时间
        member = []  # 用例负责人
        error = []  # 用例错误错
        fail = []  # 用例失败
        success = []  # 用例成功
        skip = [] # 用例跳过数
        if self.sql_data is not None:
            for first_data in range(len(self.sql_data)):
                _data = self.sql_data[first_data]
                for second_data in range(len(_data)):
                    if first_data == 0:
                        if second_data == 12:
                            case_messages['start_time'] = _data[second_data]
                    if second_data == 6:
                        if _data[second_data] == "错误":
                            error.append(_data[second_data])
                        elif _data[second_data] == "成功":
                            success.append(_data[second_data])
                        elif _data[second_data] == "失败":
                            fail.append(_data[second_data])
                        elif _data[second_data] == "跳过":
                            skip.append(_data[second_data])
                    if second_data == 9:
                        if _data[second_data] != 'None':
                            sql_data.append(float(_data[second_data][:-1]))
                    if second_data == 11:
                        member.append(_data[second_data])
                    if first_data == len(self.sql_data) - 1:
                        if second_data == 12:
                            case_messages['end_time'] = _data[second_data]
            if sql_data and member:
                case_messages["short_time"] = min(sql_data)
                case_messages["long_time"] = max(sql_data)
                case_messages["member"] = list(set(member))
            case_messages["testsRun"] = len(error) + len(fail) + len(success) + len(skip)
            case_messages["errors"] = len(error)
            case_messages["failures"] = len(fail)
            case_messages["success"] = len(success)
            case_messages['skipped'] = len(skip)
            if case_messages:
                return case_messages
        else:
            raise SQLDataError(FUN_NAME(self.current_path))

    def case_data_handle(self):
        """用例数据处理"""
        global module, is_case, da
        skipped = [] # 跳过用例封装的数据
        if self.case_data is not None:
            for skip in self.case_data.skipped:
                for da in skip:
                    if "test_" in str(da):
                        module = str(da).split(' ')[-1].split('.')[-1].split(')')[0]
                        is_case = str(da).split(' ')[0]
                    else:
                        if not da:
                            da = "未说明跳过原因..."
                        skipped.append({"module": module, "case_name": is_case,
                                        "reason": "跳过原因: {}".format(da),
                                        "insert_time": time.strftime('%Y-%m-%d %H:%M:%S')})
            self._insert_case_data(data=skipped)

    def _insert_case_data(self, data):
        """用例数据插入sql"""
        if data:
            for is_data in data:
                self.sql.insert_data(id=None, level=None, module=is_data["module"], name=is_data["case_name"],
                                     remark=None, wait_time=None, status="跳过", url=None,
                                     insert_time=is_data["insert_time"], img=None, error_reason=is_data["reason"],
                                     author=None, results_value=None)

