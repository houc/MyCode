from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
from model.DriverParameter import browser
import time

def test():
    driver = OperationElement(browser())
    try:
        driver.get('https://www.baidu.com')
        attribute = (By.XPATH, "//input[@id='su']")
        driver.del_attributed(attribute, 'value')
        time.sleep(2)
        driver.set_attributed(attribute, 'value', '卧槽一下')
        time.sleep(2)
        url = driver.get_url()
        print(url)
        time.sleep(2)
        driver.switch_iframe(attribute)
    except: raise
    finally: driver.driver_quit()

test()