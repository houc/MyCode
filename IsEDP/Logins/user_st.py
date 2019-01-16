import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import LoginTestModules

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class LoginTest(UnitTests):  
    def test_accountErrorsa(self):
        """
        错误的用户名:
        1、输入错误的用户名,
        2、点击确定并断言,
        3、也许错误了吧
        """
        try:
            self.level = 'P1'
            self.author = ['小花', '小王']
            elements = LoginTestModules(self.driver, self.url)
            self.first = elements.accountErrorsa(self.urls)
            self.second = 'user {} not exist'.format()
        except Exception as exc:
            self.error = str(exc)
            
    def test_number(self):
        """
        你猜我猜不猜
        """
        try:
            self.level = 'P1'
            self.author = ['L', 'H']
            elements = LoginTestModules(self.driver, self.url)
            self.first = elements.number(self.urls)
            self.second = 'user {} not exist'.format()
        except Exception as exc:
            self.error = str(exc)
            
