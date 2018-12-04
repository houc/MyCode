import unittest,warnings,time
from model.my_log import Logger
from yaml_read.read_yaml import MyYaml
from .login import success_login
from .driver import browser

def setUpModule():
    """单独模块开始开始工作"""
    global driver, url
    driver = browser()
    url = MyYaml().base_url
    driver.implicitly_wait(30)
    # success_login(driver,url)

def tearDownModule():
    """单独模块结束工作"""
    driver.quit()

class MyUnittest(unittest.TestCase):
    logger = Logger()
    log = start_time = result = None
    @classmethod
    def setUpClass(cls):
        """初始化"""
        cls.driver = driver
        cls.url = url

    @classmethod
    def tearDownClass(cls):
        """类结束后的工作"""

    def setUp(self):
        """单个用例开始执行的工作"""
        warnings.filterwarnings('ignore')
        self.start_time = time.time()
        self.class_name = self.__class__.__name__
        self.case_info = self._testMethodName

    def tearDown(self):
        """单个用例完成后的结束工作"""
        end_time = time.time()
        total_time = end_time - self.start_time
        self.assertEqual(self.result,'')
        self.logger.logging_info('ClassName：%s->CaseName：%s->BackMsg：%s->TotalTime: %s' % (self.class_name,self.case_info,self.result,total_time))

if __name__ == '__main__':
    unittest.main()