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
from model.GetYamlMessages import GetConfigMessage as Get
from model.MyException import WaitTypeError, FUN_NAME
from model.TimeConversion import standard_time
from config_path.path_file import read_file
from SCRM.public import LoginTestModules

def case_id():
    """
    用例计算
    :return: 用例个数
    """
    global case_count
    case_count += 1
    return case_count

def _login_module(account=None, password=None, company=None, in_login=False):
    """
    登录信息函数的封装
    :param account: 登录账号
    :param password: 登录的密码
    :param in_login: 是否需要重新登录
    :param company: 是否同一账号存在多加公司
    :return: None
    """
    if in_login:
        if account and password is not None:
            try:
                LoginTestModules(Driver).success_login(account, password, company)
            except Exception:
                Error = traceback.format_exc()
                LOG.logging_debug(Error)
                Driver.quit()
                raise Error
        else:
            LOG.logging_debug(text)
            Driver.quit()
            raise TypeError(text)
    else:
        try:
            LoginTestModules(Driver).opens_if()
        except Exception:
            Error = traceback.format_exc()
            LOG.logging_debug(Error)
            Driver.quit()
            raise Error

def setUpModule(currentModule):
    """模块初始化"""
    global Driver, SQL, Error, LOG, wait, text
    text = "当in_login为True时，account或者password不能为None"
    LOG = Logger()
    SQL = Mysql()
    Error = None
    wait = MyYaml('implicitly_wait').config
    Driver = browser(MyYaml('browser').config)
    account = MyYaml('account').config
    password = MyYaml('password').config
    company = MyYaml('company').config
    if isinstance(wait, int):
        Driver.implicitly_wait(wait)
        Driver.set_page_load_timeout(wait * 7)
    else:
        raise WaitTypeError(FUN_NAME(os.path.dirname(__file__)))
    if 'ValidateLogin_st' not in currentModule:
        _login_module(in_login=True, account=account, password=password, company=company)
    else:
        _login_module(in_login=False)


def tearDownModule():
    """模块结束"""
    Driver.quit()
    SQL.close_sql()


class UnitTests(unittest.TestCase):
    global case_count
    # noinspection PyRedeclaration
    case_count = 0
    log = start_time = result = status = level = img = error  =  None
    first = second = author = urls = RE_LOGIN = LOGIN_INFO = MODULE = None

    @classmethod
    def setUpClass(cls):
        """判断类下面是否需要重新请求账号登录"""
        if cls.RE_LOGIN:
            account = cls.LOGIN_INFO["account"]
            password = cls.LOGIN_INFO["password"]
            company = cls.LOGIN_INFO.get("company")
            if account and password is not None:
                _login_module(in_login=True, account=account, password=password, company=company)
            else:
                raise TypeError(text)

    @classmethod
    def tearDownClass(cls):
        """"""
        pass

    def setUp(self):
        """用例初始化"""
        self.driver = Driver
        self.sql = SQL
        self.setLog = Error
        self.count = case_id()
        self.start_time = time.time()
        self.module = self.__class__.__module__
        self.class_name = self.__class__.__name__
        self.case_name = self._testMethodName
        self.case_remark = self._testMethodDoc
        print(self.case_remark)
        self.current_path = os.path.dirname(__file__)
        CASE_DATA = Get(module=self.MODULE, class_name=self.class_name, case_name=self.case_name).re()
        self.level = CASE_DATA.get("level")
        self.author = CASE_DATA.get("author")
        self.url = CASE_DATA.get("url")
        self.second = CASE_DATA.get("asserts")
        self.driver.implicitly_wait(wait)
        self.driver.set_page_load_timeout(wait * 7)
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
                                self.status, self.error, self.url, total_time, self.driver, self.class_name,
                                self.screenshots_path, self.author, self, error_path, LOG).asserts()

if __name__ == '__main__':
    unittest.main()
    y = 'dsds'
    print(y.encode().decode())