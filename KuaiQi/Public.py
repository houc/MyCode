from selenium.webdriver.common.by import By

class DriverTransmit(object):
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def success_login(self):
        self.driver.get(self.url + '/login')
        self.driver.find_elements(By.XPATH, '//input[contains(@class, "form-control")]')[0].send_keys('18712345678')
        self.driver.find_elements(By.XPATH, '//input[contains(@class, "form-control")]')[1].send_keys('123456')
        self.driver.find_elements(By.XPATH, '//input[contains(@name, "commit")]')[0].click()
        assert self.driver.find_elements(By.XPATH, '//div[contains(@class, "company_name_style")]')[
                   0].text == '乐育信息技术有限公司1乐育信息技术'
