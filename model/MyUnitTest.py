import unittest
import warnings
import time
import os

from model.Logs import Logger
from model.Yaml import MyYaml
from model.SQL import Mysql
from model.DriverParameter import browser
from model.MyAssert import MyAsserts
from IsEDP.ModuleElement import LoginModule
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
            LoginModule(Driver, URL).success_login(account, password)
        except Exception as exc:
            Error = str(exc)
            Driver.quit()
            raise
    else:
        try:
            LoginModule(Driver, URL).opens_if()
        except Exception as exc:
            Error = set(exc)
            Driver.quit()
            raise

def tearDownModule():
    """模块结束"""
    Driver.quit()
    SQL.close_sql()


class UnitTests(unittest.TestCase):
    global case_count
    case_count = 0
    logger = Logger()
    log = start_time = result = status = level = img = error = other =  None
    first = second = None

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
        self.urls = MyYaml(self.class_name).parameter_ui['url']
        self.screenshots_path = read_file('img', '{}.png'.format(self.case_name))
        if os.path.exists(self.screenshots_path):
            os.remove(self.screenshots_path)

    def tearDown(self):
        """用例结束"""
        warnings.filterwarnings('ignore')
        ExecutionTime = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.time()
        total_time = end_time - self.start_time
        self.logger.logging_debug('ExecutionTime: {}; Path：{}.{}.{}; TotalUserTime: {:.4f}s; Message: {}'.format(ExecutionTime,
                                                                                                                  self.module,
                                                                                                                  self.class_name,
                                                                                                                  self.case_name,
                                                                                                                  total_time,
                                                                                                                  self.error or self.setLog))

        asserts = MyAsserts(self.first, self.second, self.count, self.level, self.case_name, self.case_remark,
                            self.status, self.error, self.urls, total_time, self.other, self.driver, self.screenshots_path)
        asserts.asserts()
        if self.first and self.second is not None:
            self.assertEqual(self.first, self.second, msg=self.error)
        elif self.error is not None:
            raise BaseException(self.error)
        else:
            self.error = Exception
            raise {"self.first 或者 self.second在用例中不存在"}




if __name__ == '__main__':
    unittest.main()