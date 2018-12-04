from model.my_unittest import *
from selenium.webdriver.common.by import By

class T(MyUnittest):
    # @unittest.skip('发的发的发生发的非官方')
    def test_F1(self):
        self.driver.get(self.url + '/dashboard#settings')
        self.log = 'test_F1'
        self.assertEqual(3,30)

    # @unittest.skip('发的发的发生发的非官方')
    def test_F2(self):
        self.driver.get(self.url + '/dashboard#clues')
        self.log = 'test_F2'
        self.assertEqual(3,30,msg = 'ppp')

    # @unittest.skip('发的发的发生发的非官方')
    def test_F3(self):
        self.driver.get(self.url + '/dashboard#customers')
        self.log = 'test_F3'
        self.assertEqual(4,40,msg = '5555')

    # @unittest.skip('发的发的发生发的非官方')
    def test_S(self):
        self.driver.get(self.url + '/dashboard#order')
        self.log = 'test_S'
        self.assertEqual(1,1)

    def test_assert(self):
        self.driver.get(self.url + '/dashboard#customers/my/list')
        self.log = 'test_assert'
        text = self.driver.find_elements(By.XPATH,'//td[contains(@class,"table-cell list-title pop_summary columns-item renderable")]')[0].text
        self.assertEqual(str(text),'测试客户有没有')

class T888(MyUnittest):
    def test_mmm(self):
        self.driver.get(self.url + '/dashboard#started/list')
        self.log = 'test_mmm'
        self.assertEqual(1,1)

    def test_556(self):
        self.driver.get(self.url + '/dashboard#legwork-stat')
        self.log = 'test_556'
        self.assertEqual(33,33)

if __name__ == '__main__':
    unittest.main()