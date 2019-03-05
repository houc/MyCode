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
class TestLogin(UnitTests):
    """
    当RE_LOGIN = True即为需要重新登录，或者是需要切换账号登录，当RE_LOGIN为True时，需要将LOGIN_INFO的value值全填写完成，
    如果请求的账号中只有一家公司那么company中的value就可以忽略不填写，否则会报错...
    MODULE为当前运行的模块
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_accountError(self):
        """
        验证错误的用户名进行登录:
        1、用户名输入框输入:15928564314999;
        2、密码输入框输入:Li123456;
        3、点击【登录】。
        """
        try:
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.element_handle(self.element)
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.element_handle(self.get_asserts, switch=True)
        except Exception as exc:
            self.error = str(exc)

    def test_passwordError(self):
        """
        验证错误的密码登录:
        1、用户名输入框输入:15928564313;
        2、密码输入框输入:Li1234564444;
        3、点击【登录】。
        """
        try:
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.element_handle(self.element)
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.element_handle(self.get_asserts, switch=True)
        except Exception as exc:
            self.error = str(exc)

    def test_accountNull(self):
        """
        验证用户名为空格登录:
        1、用户名输入框输入:
        ;
        2、密码输入框输入:Li1234564444;
        3、点击【登录】。
        """
        try:
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.element_handle(self.element)
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.element_handle(self.get_asserts, switch=True)
        except Exception as exc:
            self.error = str(exc)

    def test_passwordNull(self):
        """
        验证密码为空格登录:
        1、用户名输入框输入:
        15928564313;
        2、密码输入框输入:
        
        ;
        3、点击【登录】。
        """
        try:
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.element_handle(self.element)
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.element_handle(self.get_asserts, switch=True)
        except Exception as exc:
            self.error = str(exc)

    def test_passwordEnglish(self):
        """
        验证密码为全英文字节登录:
        1、用户名输入框输入:
        15928564313;
        2、密码输入框输入:
        
        ASDSDSFDSFDSFSDCSDCDSFCDSFDSFDSGDSGDSGDSFGDSFSDFSD;
        3、点击【登录】。
        """
        try:
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.element_handle(self.element)
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.element_handle(self.get_asserts, switch=True)
        except Exception as exc:
            self.error = str(exc)

