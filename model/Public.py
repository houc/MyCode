from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class DriverTransmit(object):
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def success_login(self,account,password):
        ElementsParameter(self.driver,self.url).login_elements(account,password)
        assert self.driver.find_elements(By.XPATH, '//*[contains(@class, "menu-name")]')[0].text == '我的工作台'


class ElementsParameter(DriverTransmit):
    def login_elements(self,account,password):
        self.driver.get(self.url + '/#/account/login')
        self.driver.find_elements(By.XPATH, '//*[contains(@class, "mu-text-field-input")]')[0].send_keys(account)
        self.driver.find_elements(By.XPATH, '//*[contains(@class, "mu-text-field-input")]')[1].send_keys(password)
        self.driver.find_elements(By.XPATH, '//*[contains(@class, "enabled")]')[0].click()
        self.driver.find_elements(By.XPATH, '//*[contains(@class, "ivu-menu-item")]')[0].click()


    def out_login(self):
        # hovers = self.driver.find_elements(By.XPATH,'//*[contains(@id,"setting-profile")]')[0]
        # ActionChains(self.driver).move_to_element(hovers).perform()
        self.driver.find_element(By.XPATH, '//*[contains(@class, "opt_li_exit")]').click()

    def out_login_url(self):
        self.driver.get(self.url + '/#/account/login')