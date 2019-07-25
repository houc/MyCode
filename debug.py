from model.DriverParameter import browser
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
import time

def r():
    driver = OperationElement(browser())
    try:
        driver.get('https://www.baidu.com')
        driver.is_send((By.XPATH, "//input[@id='kw']"), '卧槽一下')
        driver.is_clear((By.XPATH, "//input[@id='kw']"))
        driver.is_submit((By.XPATH, "//input[@id='su']"))
        a = driver.get_current_url()
        print(a)
        time.sleep(1)
    finally:
        driver.driver_quit()
r()