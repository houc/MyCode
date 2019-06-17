from config_path.path_file import read_file
from selenium import webdriver

def browser(switch=False):
    """打开浏览器"""
    global driver
    driver_path = read_file('package', 'ChromeDriver.exe')
    if switch:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(driver_path, options=options)
        driver.set_window_size(1900, 980)
    else:
        options = None
        driver = webdriver.Chrome(driver_path, options=options)
        driver.maximize_window()
    return driver

if __name__ == '__main__':
    driver = browser(True)
    driver.get('http://ukuaiqi.com')
    driver.save_screenshot(r'D:\work_file\auto_script\UI\img\logo.png')
    driver.quit()
