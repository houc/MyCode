import unittest,warnings,time
from config_path.path_file import read_file
from selenium import webdriver
from model.my_log import Logger
from yaml_read.read_yaml import MyYaml
from .login import success_login

def setUpModule():
    """单独模块开始开始工作"""
    global driver,url
    path = read_file('package','ChromeDriver.exe')
    driver = webdriver.Chrome(path)
    url = MyYaml().base_url
    driver.implicitly_wait(30)
    success_login(driver,url)

def tearDownModule():
    """单独模块结束工作"""
    driver.quit()

class MyUnittest(unittest.TestCase):
    logger = Logger()
    log = None
    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.driver = driver
        cls.url = url

    def setUp(self):
        """单个用例开始执行的工作"""
        self.class_name = self.__class__.__name__
        self.case_info = self._testMethodName
        warnings.filterwarnings('ignore')

    def tearDown(self):
        """单个用例完成后的结束工作"""
        time.sleep(1)
        driver.get(url + '/dashboard#dashboard')
        self.logger.logging_info('CLASS_NAME：%s->CASE_NAME：%s->BACK_MSG：%s' % (self.class_name,self.case_info,self.log))

if __name__ == '__main__':
    unittest.main()