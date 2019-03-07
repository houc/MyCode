import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestStaffCustomManage(UnitTests):
    """
    当RE_LOGIN = True即为需要重新登录，或者是需要切换账号登录，当RE_LOGIN为True时，需要将LOGIN_INFO的value值全填写完成，
    如果请求的账号中只有一家公司那么company中的value就可以忽略不填写，否则会报错...
    MODULE为当前运行的模块
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_drag_and_drop(self):
        """
        员工属性管理，字段拖拽是否成功:
        1、进入员工属性管理，选择字段属性(姓名)按住;
        2、拖拽到任意位置，释放字段属性。
        """
        try:
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()

        except Exception as exc:
            self.error = str(exc)

