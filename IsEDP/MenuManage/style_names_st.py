import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import MenuManageTestModules

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class MenuManageTest(UnitTests):  
    def test_errors(self):
        """
        错误的用户名:
        1、输入错误的用户名,
        2、点击确定并断言,
        3、也许错误了吧
        """
        try:
            self.level = 'P1'
            self.author = ['小花', '小王']
            elements = MenuManageTestModules(self.driver, self.url)
            self.first = elements.errors(self.urls)
            self.second = '2'
        except Exception as exc:
            self.error = str(exc)
            
    def test_name(self):
        """
        None
        """
        try:
            self.level = 'P11'
            self.author = None
            elements = MenuManageTestModules(self.driver, self.url)
            self.first = elements.name(self.urls)
            self.second = '12'
        except Exception as exc:
            self.error = str(exc)
            
    def test_KJ_name(self):
        """
        None
        """
        try:
            self.level = 'P11'
            self.author = None
            elements = MenuManageTestModules(self.driver, self.url)
            self.first = elements.KJ(self.urls)
            self.second = '12'
        except Exception as exc:
            self.error = str(exc)
            
    def test_KJ_LK(self):
        """
        None
        """
        try:
            self.level = 'P11'
            self.author = None
            elements = MenuManageTestModules(self.driver, self.url)
            self.first = elements.KJ(self.urls)
            self.second = '12'
        except Exception as exc:
            self.error = str(exc)
            
