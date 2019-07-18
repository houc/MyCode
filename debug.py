from model.DriverParameter import browser
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By


def test_change_element():
    driver = browser()
    try:
        driver.get('https://www.baidu.com')
        get = (By.XPATH, "//input[@id='su']")
        OperationElement(driver).change_element_value(get, 'value', '卧槽一下...')
        import time
        time.sleep(5)
    finally:
        driver.quit()

test_change_element()