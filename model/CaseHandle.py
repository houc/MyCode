import os
import time

from model.MyDB import MyDB
from model.MyException import SQLDataError, FUN_NAME
from model.TimeConversion import beijing_time_conversion_unix, time_conversion


class DataHandleConversion(object):
    def __init__(self, case_data=None, sql_data=None, sql_query=None):
        self.sql = MyDB(switch=False)
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
                            sql_data.append(float(_data[second_data][:-2]))
                    if second_data == 11:
                        member.append(_data[second_data])
                    if first_data == len(self.sql_data) - 1:
                        if second_data == 12:
                            case_messages['end_time'] = _data[second_data]
            if sql_data and member:
                case_messages["short_time"] = time_conversion(min(sql_data))
                case_messages["long_time"] = time_conversion(max(sql_data))
                set_member = list(set(member))
                set_member.remove('None') if 'None' in set_member else ''
                case_messages["member"] = set_member
            case_messages["testsRun"] = len(error) + len(fail) + len(success) + len(skip)
            case_messages["errors"] = len(error)
            case_messages["failures"] = len(fail)
            case_messages["success"] = len(success)
            case_messages['skipped'] = len(skip)
            start_time = beijing_time_conversion_unix(case_messages['start_time'])
            ends_time = beijing_time_conversion_unix(case_messages['end_time'])
            case_messages['total_time'] = time_conversion(ends_time - start_time)
            if case_messages:
                return case_messages
        else:
            raise SQLDataError(FUN_NAME(self.current_path))

    def case_data_handle(self):
        """用例数据处理"""
        global module, is_case, da
        skipped = [] # 跳过用例封装的数据
        if self.case_data is not None:
            for skipp in self.case_data.skipped:
                for skip in skipp:
                    if "test_" in str(skip):
                        module = str(skip).split(' ')[-1].split('.')[-1].split(')')[0]
                        is_case = str(skip).split(' ')[0]
                    else:
                        if not skip:
                            skip = "None"
                        skipped.append({"module": module, "case_name": is_case,
                                        "reason": "跳过原因: {}".format(skip),
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


