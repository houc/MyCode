from model.my_unittest import *
from selenium.webdriver.common.by import By

class TestLoginCase(MyUnittest):
    def test_user_error(self):
        """错误的用户账号"""
        self.driver.get(self.url + '/login')
        self.driver.find_elements(By.XPATH,'//input[contains(@class, "form-control")]')[0].send_keys('187123456781')
        self.driver.find_elements(By.XPATH,'//input[contains(@class, "form-control")]')[1].send_keys('123456')
        self.driver.find_elements(By.XPATH,'//input[contains(@name, "commit")]')[0].click()
        self.result = self.driver.find_elements(By.XPATH,'//span[contains(@class, "text-dangers")]')[0].text
        # self.assertEqual(a,'手机号码或密码错误！请联系管理人员。')

    def test_password_error(self):
        """错误的用户密码"""
        self.driver.get(self.url + '/login')
        self.driver.find_elements(By.XPATH, '//input[contains(@class, "form-control")]')[0].send_keys('18712345678')
        self.driver.find_elements(By.XPATH, '//input[contains(@class, "form-control")]')[1].send_keys('1234561')
        self.driver.find_elements(By.XPATH, '//input[contains(@name, "commit")]')[0].click()
        a = self.driver.find_elements(By.XPATH, '//span[contains(@class, "text-dangers")]')[0].text
        self.assertEqual(a, '手机号码或密码错误！请联系管理人员。')
