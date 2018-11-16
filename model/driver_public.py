from cofpath.path_file import get_chrome_driver_path
from selenium import webdriver
from yaread.read_yaml import MyYaml


class Driver:
    def __init__(self):
        """初始化"""
        path = get_chrome_driver_path()
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(30)
        self.url = MyYaml().base_url
