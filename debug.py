from model.DriverParameter import browser
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By

import time

user = (By.NAME, "username")
ipu = (By.NAME, "domain")
sub = (By.XPATH, "//button[@type='submit']")

ass = (By.XPATH, "//div[contains(@class, 'not-scroll')]/div[$]")
bu = (By.XPATH, "//div[contains(@class, 'form-group dropup')]")
bu1 = (By.XPATH, "//div[contains(@class, 'form-group dropup')]/div/ul/li[6]")

def test_change_element():
    driver = OperationElement(browser())

    try:
        driver.get('http://pre-design.yun300.cn/html/login.html')
        driver.is_send(user, 'admin')
        driver.is_send(ipu, 'http://1904155033.pre-pool1-site.make.yun300.cn')
        driver.is_click(sub)
        time.sleep(10)
        driver.is_click(driver.str_conversion(ass, 1))
        time.sleep(2)
        driver.is_click((By.XPATH, "//span[text()='测试组件拖拽一下']/parent::div"))
        # driver.is_click(bu)
        # driver.is_click(bu1)
        # driver.is_click((By.XPATH, "//ul[@class='itemlist']/li[1]"))
        # driver.is_send((By.XPATH, "//div[@id='js_pageInfo']/div[1]/div/input"), '测试拖拽！')
        # driver.is_click((By.XPATH, "(//div[@class='panel-footer'])[8]/div/button"))

        time.sleep(2)
        driver.is_click(driver.str_conversion(ass, 2))
        time.sleep(2)
        e1 = (By.XPATH, "(//ul[@class='new-itemlist'])[1]/li[1]")
        driver.drag_offset(e1, 1100, 50)
        time.sleep(2)
    except:
        raise
    finally:
        driver.driver_quit()

test_change_element()