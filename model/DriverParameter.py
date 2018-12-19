import warnings

from config_path.path_file import read_file
from selenium import webdriver

def browser(switch=False):
    """打开浏览器"""
    global driver
    path = read_file('package','ChromeDriver.exe')
    if switch:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        warnings.filterwarnings('ignore')
        driver = webdriver.Chrome(path, chrome_options = options)
        driver.set_window_size(1920, 1054)
    else:
        options = None
        driver = webdriver.Chrome(path, chrome_options = options)
    return driver

if __name__ == '__main__':
    a = ['--1oad-images = false','--disk-cache = true']
    path = read_file('package', 'phantomjs.exe')
    browsers = webdriver.PhantomJS(path)
    y = browsers.get('www.baidu.con')
    print(y)