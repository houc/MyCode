import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import MenuMaTestModules

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class MenuMaTest(UnitTests):  
    def test_errors4(self):
        """
        错误的用户名:
        1、输入错误的用户名,
        2、点击确定并断言,
        3、也许错误了吧
        """
        try:
            self.level = 'P1'
            self.author = ['小花', '小王']
            elements = MenuMaTestModules(self.driver, self.url)
            self.first = elements.errors4(self.urls)
            self.second = '2'
        except Exception as exc:
            self.error = str(exc)
            
    def test_name_g(self):
        """
        错误的用户名:
        1、输入错误的用户名,
        2、点击确定并断言,
        3、也许错误了吧
        """
        try:
            self.level = 'P11'
            self.author = None
            elements = MenuMaTestModules(self.driver, self.url)
            self.first = elements.name(self.urls)
            self.second = '12'
        except Exception as exc:
            self.error = str(exc)
            
    def test_nameHH(self):
        """
        3
        """
        try:
            self.level = 'P11'
            self.author = None
            elements = MenuMaTestModules(self.driver, self.url)
            self.first = elements.nameHH(self.urls)
            self.second = '12'
        except Exception as exc:
            self.error = str(exc)
            
    def test_nameHH8555(self):
        """
        3
        """
        try:
            self.level = 'P11'
            self.author = None
            elements = MenuMaTestModules(self.driver, self.url)
            self.first = elements.nameHH8555(self.urls)
            self.second = '12'
        except Exception as exc:
            self.error = str(exc)
            
