import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation, OperationElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin(UnitTests):
    def test_accountError(self):
        """
        验证错误的用户名登录:
        1、用户名输入框输入:15928564314999
        2、密码输入框输入:Li123456
        3、点击【登录】
        """
        try:
            self.level = '低'
            self.author = '后超'
            driver = OperationElement(self.driver)
            driver.F5()
            self.urls = '/#/account/login'
            self.driver.get(self.url + self.urls)
            element = ElementLocation(self.driver)
            element.XPATH("手机号/邮箱*/../input!!send", "15928564314999")
            element.XPATH("密码*/../input!!send", "Li123456")
            element.XPATH("登录*!!click")
            self.first = element.XPATH("账号未注册*/..!!text")
            self.second = '账号未注册'
        except Exception as exc:
            self.error = str(exc)
    
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
            self.urls = '/#/account/login'
            driver = OperationElement(self.driver)
            driver.F5()
            self.driver.get(self.url + self.urls)
            element = ElementLocation(self.driver)
            element.XPATH("手机号/邮箱*/../input!!send", "15928564313")
            element.XPATH("密码*/../input!!send", "Li1234564444")
            element.XPATH("登录*!!click")
            self.first = element.XPATH("密码错误请重新输入*/..!!text")
            self.second = '密码错误请重新输入'
        except Exception as exc:
            self.error = str(exc)

    def test_switchQR(self):
        """
        验证切换二维码是否生成二维码:
        1、点击【扫码登录】
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/#/account/login'
            driver = OperationElement(self.driver)
            driver.F5()
            self.driver.get(self.url + self.urls)
            element = ElementLocation(self.driver)
            element.CSS("div[class='ivu-tabs-tab']!!click")
            self.first = element.XPATH("span$中企智营APP*/..!!text")
            self.second = '中企智营APP'
        except Exception as exc:
            self.error = str(exc)
