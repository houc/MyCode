import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from SCRM.sales_synergy.currency import SalesSynergyElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestAssign(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": 15800000448, "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_hand_in_is_exist_1(self):
        """
        验证我指派“进行中”状态是否存在
        """
        try:
            driver = SalesSynergyElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.table_text(1)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_finish_is_exist_1(self):
        """
        验证我指派“已完成”状态是否存在
        """
        try:
            driver = SalesSynergyElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.table_text(2)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_wait_accept_is_exist_1(self):
        """
        验证我指派“待我接受”状态是否存在
        """
        try:
            driver = SalesSynergyElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.table_text(3)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

