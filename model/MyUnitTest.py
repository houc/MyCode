import unittest,warnings,time
from model.Logs import Logger
from model.Yaml import MyYaml
from model.DriverParameter import browser
from SCRM.public_transmit import DriverTransmit


def setUpModule(currentModule):
    """模块初始化"""
    global Driver, URL
    Driver = browser()
    URL = MyYaml('SCRM').base_url
    account = MyYaml('account').config
    password = MyYaml('password').config
    wait = MyYaml('implicitly_wait').config
    Driver.implicitly_wait(wait)
    if 'login_st' not in currentModule:
        DriverTransmit(Driver, URL).success_login(account,password)

def tearDownModule():
    """模块结束"""
    Driver.quit()

class UnitTests(unittest.TestCase):
    logger = Logger()
    log = start_time = result = None
    @classmethod
    def setUpClass(cls):
        """类初始化"""
        cls.driver = Driver
        cls.url = URL

    @classmethod
    def tearDownClass(cls):
        """类结束"""
        return

    def setUp(self):
        """用例初始化"""
        self.data = list()
        warnings.filterwarnings('ignore')
        self.start_time = time.time()
        self.class_name = self.__class__.__name__
        self.module = self.__class__.__module__
        self.case_info = self._testMethodName
        caseMsg = MyYaml(self.case_info).case_parameter
        for i in caseMsg:
            asserts = [k for k in i['asserts']][0]
            self.data.append(asserts)               # 参数值为 0
            self.data.append(i['Initialization'])   # 参数值为 1

    def tearDown(self):
        """用例结束"""
        ExecutionTime = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.time()
        total_time = end_time - self.start_time
        self.logger.logging_debug('ExecutionTime: %s ; Path：%s.%s.%s ; TotalUserTime: %s ; Message: %s'
                                 % (ExecutionTime,self.module,self.class_name,self.case_info,total_time,self.result))
        self.assertEqual(self.result,self.data[0])

if __name__ == '__main__':
    unittest.main()