import re
import dataclasses
import typing
import time

from model.MyDB import MyDB
from . TimeConversion import standard_time


@dataclasses.dataclass
class MyAsserts:

    case_catalog: str
    case_level: str
    case_module: str
    case_name: str
    case_url: str
    case_scene: str
    # case_status: str  # 判断的！不作为传参处理！
    case_results: str
    # case_error_reason: str
    case_insert_parameter: str
    case_wait_time: time
    case_img: str
    case_author: str
    case_remark: str

    log: typing.Any
    assert_first: str
    error_path: str
    encoding: str = 'utf-8'

    def __post_init__(self):
        if self.case_insert_parameter:
            self.insert = self.str_conversion(self.case_insert_parameter)
        else:
            self.insert = None
        self.insert_time = standard_time()

    def asserts_eq(self):
        self._insert_sql(status=None, img=self.case_img, reason=self.case_results)

    def _insert_sql(self, status, img, reason):
        MyDB().insert_data(case_catalog=self.case_catalog, case_level=self.case_level,
                            case_module=self.case_module, case_name=self.case_name,
                            case_url=self.case_url, case_scene=self.str_conversion(self.case_scene),
                            case_status=status, case_results=self.str_conversion(self.case_results),
                            case_error_reason=reason,
                            case_insert_parameter=self.insert,
                            case_wait_time=f'{self.case_wait_time :.2f}',
                            case_img=img, case_author=self.case_author,
                            case_remark=self.str_conversion(self.case_remark),
                            insert_time=self.insert_time)

    @staticmethod
    def str_conversion(values: str):
        return re.sub("'", "`", str(values)).replace('\\', '/').replace('"', "`").replace('%', '//')

    def _log(self, reason):
        self.log.info(f'错误路径:{self.error_path},错误原因:{reason}')

