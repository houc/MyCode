from config_path.path_file import read_file
from selenium import webdriver

def browser(switch=False):
    """打开浏览器"""
    path = read_file('package','ChromeDriver.exe')
    if switch is True:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
    else:
        options = None
    driver = webdriver.Chrome(path,chrome_options = options)
    driver.set_window_size(1920,1054)
    return driver

if __name__ == '__main__':
    a = ['--1oad-images = false','--disk-cache = true']
    path = read_file('package', 'phantomjs.exe')
    browsers = webdriver.PhantomJS(path)
    y = browsers.get('www.baidu.con')
    print(y)