from selenium.webdriver.common.by import By
from model.Yaml import MyYaml


class DriverTransmit(object):
    def __init__(self, driver, url):
        """初始化"""
        self.driver = driver
        self.url = url
        self.yaml = MyYaml('Login').parameter_ui['url']

    def _asserts(self):
        self.driver.get(self.url + self.yaml)
        asserts = self.xpath('btn-login').text
        return asserts

    def xpathS(self, parameter, type='@class', tag='*'):
        """xpath多元素定位"""
        return self.driver.find_elements(By.XPATH, '//{}[contains({}, "{}")]'.format(tag, type, parameter))

    def cssS(self, css):
        """css多元素定位"""
        return self.driver.find_elements(By.CSS_SELECTOR, '.{}'.format(css))

    def id(self, id):
        """id定位"""
        return self.driver.find_element(By.ID, '{}'.format(id))

    def xpath(self, parameter, type='@class', tag='*'):
        """xpath单元素定位"""
        return self.driver.find_element(By.XPATH, '//{}[contains({}, "{}")]'.format(tag, type, parameter))


if __name__ == '__main__':
    Test = DriverTransmit('','')
    print(Test.xpathS('2'))