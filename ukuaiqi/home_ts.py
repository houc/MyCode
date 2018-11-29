from model.my_unittest import MyUnittest
from selenium.webdriver.common.by import By
import unittest,time

class T(MyUnittest):
    @unittest.skip('发的发的发生发的非官方')
    def test_F1(self):
        self.driver.get(self.url + '/dashboard#settings')
        self.assertEqual(3,30)
        print(55)

    @unittest.skip('发的发的发生发的非官方')
    def test_F2(self):
        self.driver.get(self.url + '/dashboard#clues')
        self.assertEqual(3,30,msg = 'ppp')

    @unittest.skip('发的发的发生发的非官方')
    def test_F3(self):
        self.driver.get(self.url + '/dashboard#customers')
        self.assertEqual(4,40,msg = '5555')

    @unittest.skip('发的发的发生发的非官方')
    def test_S(self):
        self.driver.get(self.url + '/dashboard#order')
        self.assertEqual(1,1)

    def test_assert(self):
        self.driver.get(self.url + '/dashboard#customers/my/list')
        text = self.driver.find_elements(By.XPATH,'//td[contains(@class,"table-cell list-title pop_summary columns-item renderable")]')[0].text
        self.assertEqual(str(text),'测试客户有没有')

if __name__ == '__main__':
    unittest.main()