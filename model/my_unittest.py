import unittest,time,warnings
from cofpath.path_file import get_chrome_driver_path
from selenium import webdriver
from yaread.read_yaml import MyYaml


class MyUnittest(unittest.TestCase):
    driver,start_mk,start_time = None,None,None
    @classmethod
    def setUpClass(self):
        """初始化"""
        self.start_mk = time.time()
        self.start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        path = get_chrome_driver_path()
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(30)
        self.url = MyYaml().base_url

    @classmethod
    def tearDownClass(self):
        """所有用例测试完成后的结束工作"""
        self.end_mk = time.time()
        self.end_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.total_finish_time = self.end_mk - self.start_mk
        self.driver.quit()

    def setUp(self):
        """单个用例开始执行的工作"""
        warnings.simplefilter("ignore")
        self.root_time = time.time()


    def tearDown(self):
        """单个用例完成后的结束工作"""
        self.finish_time = time.time()
        self.unit_time = self.finish_time - self.root_time


if __name__ == '__main__':
    unittest.main()