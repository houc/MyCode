import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from SCRM.ModuleElement import TestLoginModules

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin(UnitTests):  
    def test_accountError(self):
        """
        验证错误的用户名登录:
        1、用户名输入框输入{}，
        2、密码输入框输入{}，
        3、点击【登录】
        """
        try:
            self.level = '低'
            self.author = []
            elements = TestLoginModules(self.driver, self.url)
            self.first = elements.accountError(self.urls)
            self.second = 'True'
        except Exception as exc:
            self.error = str(exc)
            
    def test_accountLong(self):
        """
        None
        """
        try:
            self.level = '高'
            self.author = []
            elements = TestLoginModules(self.driver, self.url)
            self.first = elements.accountLong(self.urls)
            self.second = ''
        except Exception as exc:
            self.error = str(exc)
            

