import unittest,warnings,time
from model.Logs import Logger
from model.Yaml import MyYaml
from model.DriverParameter import browser
from SCRM.public_transmit import DriverTransmit
from model.SQL import Mysql

def case_id():
    """用例计算"""
    global case_count
    case_count += 1
    return case_count

def setUpModule(currentModule):
    """模块初始化"""
    global Driver, URL,SQL
    Browser = MyYaml('browser').config
    account = MyYaml('account').config
    password = MyYaml('password').config
    wait = MyYaml('implicitly_wait').config
    Driver = browser(Browser)
    SQL = Mysql()
    URL = MyYaml('SCRM').base_url
    Driver.implicitly_wait(wait)
    if 'login_st' not in currentModule:
        DriverTransmit(Driver, URL).success_login(account,password)
    else:
        DriverTransmit(Driver,URL).opens_if()

def tearDownModule():
    """模块结束"""
    Driver.quit()
    SQL.close_sql()

class UnitTests(unittest.TestCase):
    global case_count
    case_count = 0
    logger = Logger()
    log = start_time = result = error = status = img = None
    @classmethod
    def setUpClass(cls):
        """类初始化"""
        cls.driver = Driver
        cls.url = URL
        cls.sql = SQL

    @classmethod
    def tearDownClass(cls):
        """类结束"""
        return

    def setUp(self):
        """用例初始化"""
        self.data = list()
        self.count = case_id()
        warnings.filterwarnings('ignore')
        self.start_time = time.time()
        self.module = self.__class__.__module__
        self.class_name = self.__class__.__name__
        self.case_name = self._testMethodName
        self.case_remark = self._testMethodDoc
        caseMsg = MyYaml(self.case_name).case_parameter
        for i in caseMsg:
            asserts = [k for k in i['asserts']][0]
            self.data.append(asserts)               # 参数值为 0
            self.data.append(i['Initialization'])   # 参数值为 1
            self.data.append(i['url'])              # 参数值为 2
            self.data.append(i['level'])            # 参数值为 3

    def tearDown(self):
        """用例结束"""
        ExecutionTime = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.time()
        total_time = end_time - self.start_time
        self.logger.logging_debug('ExecutionTime: %s ; Path：%s.%s.%s ; TotalUserTime: %s ; Message: %s'% (
                                 ExecutionTime,self.module,self.class_name,self.case_name,
                                 total_time,self.result))
        self.sql.insert_data(self.count,self.data[3],self.case_name,
                             self.case_remark,total_time,self.status,
                             self.data[2],self.img,self.error)

if __name__ == '__main__':
    unittest.main()