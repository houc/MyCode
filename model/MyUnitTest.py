import unittest,warnings,time
from model.Logs import Logger
from model.Yaml import MyYaml
from model.DriverParameter import browser
from KuaiQi.Public import DriverTransmit


def setUpModule():
    """模块初始化"""
    global driver, url
    driver = browser()
    url = MyYaml().base_url
    driver.implicitly_wait(20)
    DriverTransmit(driver, url).success_login()

def tearDownModule():
    """模块结束"""
    driver.quit()

class UnitTest(unittest.TestCase):
    logger = Logger()
    log = start_time = result = None
    @classmethod
    def setUpClass(cls):
        """类初始化"""
        cls.driver = driver
        cls.url = url

    @classmethod
    def tearDownClass(cls):
        """类结束"""
        return

    def setUp(self):
        """用例初始化"""
        warnings.filterwarnings('ignore')
        self.start_time = time.time()
        self.class_name = self.__class__.__name__
        self.module = self.__class__.__module__
        self.case_info = self._testMethodName

    def tearDown(self):
        """用例结束"""
        end_time = time.time()
        total_time = end_time - self.start_time
        self.logger.logging_debug('Path：%s.%s.%s ; TotalUserTime: %s ; Message: %s'
                                 % (self.module,self.class_name,self.case_info,total_time,self.result))

if __name__ == '__main__':
    unittest.main()