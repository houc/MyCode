import unittest
import time

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestStaffCustomManage(UnitTests):
    """
    当RE_LOGIN = True即为需要重新登录，或者是需要切换账号登录，当RE_LOGIN为True时，需要将LOGIN_INFO的value值全填写完成，否则会报错...
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    
    def test_drag_and_drop(self):
        """
        员工属性管理，字段拖拽是否成功:
        1、进入员工属性管理，选择字段属性(姓名)按住;
        2、拖拽到任意位置，释放字段属性。
        """
        try:
            self.level = '中'
            self.author = '后超'
            self.urls = '/platform/#/manage/employeeProperty'
            self.second = '属性排序成功'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.CSS("span > tr:nth-child(1)!!dragF")
            driver.CSS("span > tr:nth-child(2)!!dragS")
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.XPATH("//*[text()='属性排序成功']/.!!text")
        except Exception as exc:
            self.error = str(exc)

