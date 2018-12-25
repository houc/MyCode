import unittest

from model.MyUnitTest import setUpModule,tearDownModule,UnitTests
from IsEDP.ModuleElement import MenuModule


class MenuManager(UnitTests):
    @unittest.skip('跳过')
    def test_createMenuNull(self):
        """创建菜单，不键入任何值"""
        self.level = 'P0'
        elements = MenuModule(self.driver,self.url)
        elements.CreateMenuNull(self.urls)
        self.assertEqual(elements.asserts,'menu name cannot be empty')

    # @unittest.skip('跳过Start')
    def test_createNull(self):
        """创建菜单字段为空"""
        self.first = 1
        self.second = 2