from config_path.path_file import read_file
from selenium import webdriver

def browser():
    """打开浏览器"""
    path = read_file('package','ChromeDriver.exe')
    driver = webdriver.Chrome(path)
    return driver

if __name__ == '__main__':
    # a = ['--1oad-images = false','--disk-cache = true']
    # path = read_file('package', 'phantomjs.exe')
    # browsers = webdriver.PhantomJS(path)
    # y = browsers.get('www.baidu.con')
    # print(y)
    browser()