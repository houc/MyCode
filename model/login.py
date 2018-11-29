from selenium.webdriver.common.by import By

def success_login(driver,url):
    driver.get(url + '/login')
    driver.find_elements(By.XPATH,'//input[contains(@class, "form-control")]')[0].send_keys('18712345678')
    driver.find_elements(By.XPATH,'//input[contains(@class, "form-control")]')[1].send_keys('123456')
    driver.find_elements(By.XPATH,'//input[contains(@name, "commit")]')[0].click()
    assert driver.find_elements(By.XPATH, '//div[contains(@class, "company_name_style")]')[0].text == '乐育信息技术有限公司1乐育信息技术'
