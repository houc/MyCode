# @Time             : 2019/8/23 16:44
# @Author           : hc
# @FileName         : ElementSupport.py
# @Tool             : PyCharm
# @Target           : UI

__author__ = 'hc'

from selenium.webdriver.support import expected_conditions as EC


class GetCurrentUrl(object):
    def __call__(self, driver):
        return driver.current_url


class PureClick(object):
    def __init__(self, element):
        self.by = element

    def __call__(self, driver):
        element = EC._find_element(driver, self.by)
        element.click()


class WebIsOpen(object):
    def __init__(self, title):
        self.title = title

    def __call__(self, driver):
        return driver.title
