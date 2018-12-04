from config_path.path_file import read_file
from selenium import webdriver

def browser():
    """打开浏览器"""
    path = read_file('package','ChromeDriver.exe')
    driver = webdriver.Chrome(path)
    return driver