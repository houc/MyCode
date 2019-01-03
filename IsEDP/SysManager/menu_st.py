import unittest
import os

from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import MenuModule

_PATH = os.path.realpath(__file__)
_SKIP = Skip(current_module(_PATH)).is_skip


@unittest.skipIf(_SKIP, '还未定义')
class MenuManager(UnitTests):
    def test_createMenuNull(self):
        """创建菜单，不键入任何值"""
        self.level = 'P0'
        elements = MenuModule(self.driver,self.url)
        elements.CreateMenuNull(self.urls)

    def test_createNull(self):
        """创建菜单字段为空"""
        self.first = 1
        self.second = 2


if __name__ == '__main__':
    unittest.main()