from model.MyUnitTest import *
from model.Public import ElementsParameter
from selenium.webdriver.common.by import By
import time,unittest

class LoginTestIn(UnitTests):
    def test_accountError(self):
        elements = ElementsParameter(self.driver,self.url)
        elements.out_login()
        time.sleep(2)
        # elements.login_elements('14012345687','123456')
        # self.result = self.driver.find_elements(By.XPATH,'//*[contains(@class,"text-dangers")]')[0].text
        # self.assertEqual(self.result,'手机号码或密码错误！请联系管理人员。')

    def test_accountSort(self):
        elements = ElementsParameter(self.driver, self.url)
        elements.out_login_url()
        time.sleep(2)
        # elements.login_elements('14012345687' * 12, '123456')
        # self.result = self.driver.find_elements(By.XPATH, '//*[contains(@class,"text-dangers")]')[0].text
        # self.assertEqual(self.result, '手机号码或密码错误！请联系管理人员。')

if __name__ == '__main__':
    unittest.main()