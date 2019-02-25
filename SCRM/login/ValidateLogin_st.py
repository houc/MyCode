import unittest
import time
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin(UnitTests):
    def test_accountError(self):
        """
        验证错误的密码进行登录:
        1、用户名输入框输入:15928564314999
        2、密码输入框输入:Li123456
        3、点击【登录】
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "15928564314999")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "Li123456")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.first = driver.XPATH("//*[text()='账号未注册']/..!!text")
            self.second = '账号未注册'
        except Exception:
            self.error = str(traceback.print_exc())

    def test_passwordError(self):
        """
        验证错误的密码登录:
        1、用户名输入框输入:15928564313
        2、密码输入框输入:Li1234564444
        3、点击【登录】
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "15928564313")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "Li1234564444")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.first = driver.XPATH("//*[text()='密码错误请重新输入']/..!!text")
            self.second = '密码错误请重新输入'
        except Exception:
            self.error = str(traceback.print_exc())

