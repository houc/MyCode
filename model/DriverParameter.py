import warnings

from config_path.path_file import read_file
from selenium import webdriver

def browser(switch=False):
    """打开浏览器"""
    global driver
    path = read_file('package', 'ChromeDriver.exe')
    if switch:
        warnings.filterwarnings('ignore')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(path, chrome_options=options)
        driver.set_window_size(1920, 1054)
    else:
        options = None
        driver = webdriver.Chrome(path, chrome_options=options)
        driver.maximize_window()
    return driver

if __name__ == '__main__':
    import time
    from selenium.webdriver.common.keys import Keys

    fil = read_file('img', '{}.png'.format(5))
    driver = browser(True)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1054)
    driver.set_page_load_timeout(60)
    driver.get('http://www.baidu.com')
    time.sleep(3)
    driver.save_screenshot(fil)
    driver.quit()
    # driver.set_window_size(200, 500)
    # driver.get('https://www.scrm365.cn/#/account/login')
    # js = 'document.getElementsByClassName("mu-text-field-input")[0].value="15928564313"'
    # driver.execute_script(js)
    # # driver.find_elements_by_xpath('//*[contains(@class,"mu-text-field-input")]')[0].send_keys('15928564313')
    # driver.find_elements_by_xpath('//*[contains(@class,"mu-text-field-input")]')[1].send_keys('Li123456')
    # driver.find_elements_by_xpath('//*[contains(@class,"enabled")]')[0].click()
    # driver.find_elements_by_xpath('//*[contains(@class,"ivu-menu-item")]')[0].click()
    # time.sleep(2)
    # driver.execute_script('document.getElementsByClassName("iconfont-s ics-bangzhuzhongxin")')
    # time.sleep(2)
    # driver.quit()
    # with driver:
    #     driver.get('https://testapi.edpglobal.cn:8443/#/system/navbarManage')
    #     j = driver.find_elements_by_xpath('//div[contains(@class,"side-nav left")]')[0].is_displayed()
    #     # js = "arguments[0].scrollIntoView();"
    #     # time.sleep(3)
    #     # driver.execute_script(js, j)
    #     time.sleep(1)
    #     # js = "var q=document.getElementById('id').scrollTop=1000"
    #     j = driver.find_elements_by_tag_name('button')
    #     for i in j:
    #         print(i.get_attribute('class'))


