from model.DriverParameter import browser
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
import time

def r():
    driver = OperationElement(browser())
    try:
        driver.get('https://www.baidu.com')
        driver.send_keys((By.XPATH, "//input[@id='kw']"), '卧槽一下')
        # driver.is_clear((By.XPATH, "//input[@id='kw']"))
        h = driver.submit((By.XPATH, "//input[@id='su']"))
        time.sleep(1)
        a = driver.get_current_url()
        print(a)
        time.sleep(1)
    finally:
        driver.driver_quit()
r()