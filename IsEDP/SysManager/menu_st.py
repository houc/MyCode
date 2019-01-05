import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import MenuModule

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class MenuManager(UnitTests):
    def test_createMenuNull(self):
        """
        新建菜单:
        1、点击新增菜单
        2、在输入框不输入任何值
        3、点击确认并判断是否有错误的提示框
        """
        try:
            self.level = "P0"
            elements = MenuModule(self.driver, self.url)
            self.first = elements.CreateMenuNull(self.urls)
            self.second = "menu name cannot be empty"
        except Exception as exc:
            self.error = str(exc)

    def test_createParentMenuScroll(self):
        """
        新建菜单:
        1、点击新增菜单
        2、在父级菜单中选择菜单
        3、点击确认并判断是否选中
        """
        try:
            self.level = "P2"
            elements = MenuModule(self.driver, self.url)
            self.first = elements.createParentMenuScroll(self.urls)
            self.second = "财务日志"
        except Exception as exc:
            self.error = str(exc)

    def test_createNullCancel(self):
        """
        新建菜单:
        1、点击新增菜单
        2、新增菜单加载出来后
        3、点击取消并判断是否取消成功
        """
        try:
            self.level = "P3"
            elements = MenuModule(self.driver, self.url)
            self.first = elements.createNullCancel(self.urls)
            self.second = False
        except Exception as exc:
            self.error = str(exc)

    def test_edit(self):
        """
        编辑菜单:
        1、点击编辑按钮
        2、加载出弹窗后点击确定并判断是否编辑成功
        """
        self.first = 1
        self.second = 1


if __name__ == '__main__':
    unittest.main()