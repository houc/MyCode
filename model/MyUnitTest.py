import unittest
import traceback
import warnings
import time
import os

from model.Logs import Logger
from model.Yaml import MyYaml
from model.SQL import Mysql
from model.DriverParameter import browser
from model.MyAssert import MyAsserts
from model.MyException import WaitTypeError, FUN_NAME
from model.TimeConversion import standard_time
from config_path.path_file import read_file
from SCRM.public import LoginTestModules

def case_id():
    """用例计算"""
    global case_count
    case_count += 1
    return case_count

def setUpModule(currentModule):
    """模块初始化"""
    global Driver, URL, SQL, Error, LOG, wait
    LOG = Logger()
    Browser = MyYaml('browser').config
    account = MyYaml('account').config
    password = MyYaml('password').config
    wait = MyYaml('implicitly_wait').config
    Driver = browser(Browser)
    SQL = Mysql()
    URL = MyYaml('SCRM').base_url
    Error = None
    if isinstance(wait, int):
        Driver.implicitly_wait(wait)
    else:
        raise WaitTypeError(FUN_NAME(os.path.dirname(__file__)))
    if 'ValidateLogon_st' not in currentModule:
        try:
            LoginTestModules(Driver, URL).success_login(account, password)
        except Exception:
            Error = traceback.format_exc()
            LOG.logging_debug(Error)
            Driver.quit()
    else:
        try:
            LoginTestModules(Driver, URL).opens_if()
        except Exception:
            Error = traceback.format_exc()
            LOG.logging_debug(Error)
            Driver.quit()

def tearDownModule():
    """模块结束"""
    Driver.quit()
    SQL.close_sql()


class UnitTests(unittest.TestCase):
    global case_count
    case_count = 0
    log = start_time = result = status = level = img = error = other =  None
    first = second = author = None

    def setUp(self):
        """用例初始化"""
        Driver.implicitly_wait(wait)
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
        self.current_path = os.path.dirname(__file__)
        self.urls = MyYaml(self.class_name).parameter_ui['url']
        self.author = MyYaml(self.class_name).parameter_ui['author']
        self.current_time = standard_time()
        self.screenshots_path = read_file('img', '{}.png'.format(self.case_name))
        if self.setLog is not None:
            LOG.logging_debug('执行时间:{}, 错误路径:{}, 错误信息:{}'.
                                      format(self.current_time, self.current_path, self.setLog))

    def tearDown(self):
        """用例结束"""
        warnings.filterwarnings('ignore')
        end_time = time.time()
        total_time = end_time - self.start_time
        error_path = '{}/{}/{}'.format(self.module, self.class_name, self.case_name)
        MyAsserts(self.first, self.second, self.count, self.level, self.case_name, self.case_remark,
                                self.status, self.error, self.urls, total_time, self.other, self.driver,
                                self.screenshots_path, self.author, self, error_path, LOG).asserts()

if __name__ == '__main__':
    unittest.main()