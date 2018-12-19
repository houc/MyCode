import unittest
import warnings
import time
import os

from model.Logs import Logger
from model.Yaml import MyYaml
from model.DriverParameter import browser
from IsEDP.ModuleElement import LoginModule
from model.SQL import Mysql
from config_path.path_file import read_file

def case_id():
    """用例计算"""
    global case_count
    case_count += 1
    return case_count

def setUpModule(currentModule):
    """模块初始化"""
    global Driver, URL,SQL,Error
    Browser = MyYaml('browser').config
    account = MyYaml('account').config
    password = MyYaml('password').config
    wait = MyYaml('implicitly_wait').config
    Driver = browser(Browser)
    SQL = Mysql()
    URL = MyYaml('EDP').base_url
    Error = None
    Driver.implicitly_wait(wait)
    if 'login_st' not in currentModule:
        try:
            LoginModule(Driver, URL).success_login(account,password)
        except Exception as e:
            Error = e
            Driver.quit()
    else:
        try:
            LoginModule(Driver,URL).opens_if()
        except Exception as e:
            Error = e
            Driver.quit()

def tearDownModule():
    """模块结束"""
    Driver.quit()
    SQL.close_sql()


class UnitTests(unittest.TestCase):
    global case_count
    case_count = 0
    logger = Logger()
    log = start_time = result = status = level = img = error = other =  None

    def setUp(self):
        """用例初始化"""
        self.driver = Driver
        self.url = URL
        self.sql = SQL
        self.setLog = Error
        self.count = case_id()
        self.start_time = time.time()
        self.module = self.__class__.__module__
        self.class_name = self.__class__.__name__
        self.case_name = self._testMethodName
        self.case_remark = self._testMethodDoc
        self.urls = MyYaml(self.class_name).parameter['url']
        self.screenshots_path = read_file('img','{}.png'.format(self.case_name))
        if os.path.exists(self.screenshots_path):
            os.remove(self.screenshots_path)

    def tearDown(self):
        """用例结束"""
        warnings.filterwarnings('ignore')
        ExecutionTime = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.time()
        total_time = end_time - self.start_time
        self.logger.logging_debug('ExecutionTime: %s ; Path：%s.%s.%s ; TotalUserTime: %.4fs ; Message: %s'% (
                                 ExecutionTime,self.module,self.class_name,self.case_name,
                                 total_time,self.error or self.setLog))
        if os.path.exists(self.screenshots_path):
            self.img = self.screenshots_path
        # if '!=' in str(self.error):
        #     self.status = '失败'
        # elif self.error is None:
        #     self.status = '成功'
        # else:
        #     self.status = '错误'
        # if self.setLog is None:
        #     self.sql.insert_data(self.count,self.level,self.case_name,
        #                          self.case_remark,"%.4fs"%total_time,self.status,
        #                          self.urls,self.img,self.error,self.other)


if __name__ == '__main__':
    unittest.main()