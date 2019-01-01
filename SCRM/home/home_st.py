from model.MyUnitTest import UnitTests,setUpModule,tearDownModule
from SCRM.home.public import ElementsParameter
import unittest


class HomeTestIn(UnitTests):
    def test_search(self):
        """工作台中快速进入搜索界面"""
        elements = ElementsParameter(self.driver, self.url)
        elements.home_search(self.data[2])
        self.result = elements.xpathS('global-title')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_helpCenter(self):
        """工作台中快速进入帮助中心界面"""
        elements = ElementsParameter(self.driver, self.url)
        elements.help_center(self.data[2])
        self.result = elements.xpathS('list-title')[0].text
        self.assertEqual(self.result, self.data[0])

if __name__ == '__main__':
    unittest.main()
