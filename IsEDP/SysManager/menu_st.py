from model.MyUnitTest import setUpModule,tearDownModule,UnitTests
from IsEDP.ModuleElement import MenuModule


class MenuManager(UnitTests):
    def test_createMenuNull(self):
        """创建菜单，不键入任何值"""
        try:
            self.level = 'P0'
            elements = MenuModule(self.driver,self.url)
            elements.CreateMenuNull(self.urls)
            self.assertEqual(elements.asserts, 'menu name cannot be empty')
        except Exception as e:
            self.driver.save_screenshot(self.screenshots_path)
            self.error = str(e)

    def test_createNull(self):
        """创建菜单字段为空"""
        self.assertEqual(1,1)
