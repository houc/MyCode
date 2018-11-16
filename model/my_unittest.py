import unittest,time,warnings
from model.driver_public import Driver
from model.login import Login

class MyUnittest(unittest.TestCase):
    driver,start_mk,start_time = None,None,None
    @classmethod
    def setUpClass(self):
        """初始化"""
        self.start_mk = time.time()
        self.start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.driver = Driver().driver
        self.url = Driver().url

    @classmethod
    def tearDownClass(self):
        """所有用例测试完成后的结束工作"""
        self.end_mk = time.time()
        self.end_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.driver.quit()

    def setUp(self):
        """单个用例开始执行的工作"""
        warnings.simplefilter("ignore")
        self.root_time = time.time()


    def tearDown(self):
        """单个用例完成后的结束工作"""
        self.finish_time = time.time()
        print(self.finish_time - self.root_time)

if __name__ == '__main__':
    unittest.main()