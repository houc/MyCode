import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from SCRM.login.currency import LoginElement
from SCRM.common import LoginPublic

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin_3(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_test_repeat_login_15(self):
        """
        测试循环登录，用例时长
        1、输入账号{15882223197}，输入密码{Po123456};
        2、点击登录;
        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_test_repeat_login_16(self):
        """
        测试循环登录，用例时长
        1、输入账号{15882223197}，输入密码{Po123456};
        2、点击登录;
        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_test_repeat_login_17(self):
        """
        测试循环登录，用例时长
        1、输入账号{15882223197}，输入密码{Po123456};
        2、点击登录;
        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_test_repeat_login_18(self):
        """
        测试循环登录，用例时长
        1、输入账号{15882223197}，输入密码{Po123456};
        2、点击登录;
        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_test_repeat_login_19(self):
        """
        测试循环登录，用例时长
        1、输入账号{15882223197}，输入密码{Po123456};
        2、点击登录;
        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

