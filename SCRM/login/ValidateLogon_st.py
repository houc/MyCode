import unittest

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
        验证错误的用户名登录:
        1、用户名输入框输入:15928564313
        2、密码输入框输入:Li123456
        3、点击【登录】
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = self.url + '/user/login'
            self.driver.get(self.urls)
            element = ElementLocation(self.driver)
            element.XPATH("客户管理*/../div[1]!!send", "15928564313")
            element.CSS("po[name='5']")
            element.XPATH("对对对*/..")
            element.XPATH("下火*/../div[3]!!click")
            self.first = element.XPATH("小同学*text")
            self.second = '好好把'
        except Exception as exc:
            self.error = str(exc)

    def test_accountLong(self):
        """
        测试:
        1、这是一段代码
        2、点击【None】
        """
        try:
            self.level = '高'
            self.author = '后超'
            self.urls = self.url + '/user/login'
            self.driver.get(self.urls)
            element = ElementLocation(self.driver)
            element.CSS("input[class='wd']!!click")
            element.CSS("div[name='KK']!!send", "4444")
            self.first = element.CSS("div[name='8']!!text")
            self.second = True
        except Exception as exc:
            self.error = str(exc)

    def test_mast(self):
        """
        None
        """
        try:
            self.level = '中'
            self.author = '小明'
            self.urls = self.url + '/k/g/g/g/'
            self.driver.get(self.urls)
            element = ElementLocation(self.driver)
            element.CSS("input[class='wd']!!click")
            element.CSS("div[name='KK']!!send", "4444")
            element.XPATH("客户管理*/../div[1]!!send", "15928564313")
            element.CSS("po[name='5']")
            element.XPATH("对对对*/..")
            element.XPATH("下火*/../div[3]!!click")
            self.first = element.CSS("div[name='8']!!text")
            self.second = '数据'
        except Exception as exc:
            self.error = str(exc)

