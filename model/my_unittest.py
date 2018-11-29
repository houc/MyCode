import unittest,warnings
from cofpath.path_file import get_chrome_driver_path
from selenium import webdriver
from yaread.read_yaml import MyYaml
from .login import success_login


class MyUnittest(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        """初始化"""
        path = get_chrome_driver_path()
        cls.driver = webdriver.Chrome(path)
        cls.driver.implicitly_wait(35)
        cls.url = MyYaml().base_name
        success_login(cls.driver,cls.url)

    @classmethod
    def tearDownClass(cls):
        """所有用例测试完成后的结束工作"""
        cls.driver.quit()

    def setUp(self):
        """单个用例开始执行的工作"""
        warnings.simplefilter("ignore")

    def tearDown(self):
        """单个用例完成后的结束工作"""
        self.driver.get(self.url + '/dashboard#dashboard')

if __name__ == '__main__':
    unittest.main()