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
from model.PrintColor import RED_BIG
from model.MyException import LoginError, LogErrors, LoginSelectError
from config_path.path_file import read_file
from SCRM.public import LoginTestModules

def _case_id():
    """
    用例计算
    :return: 用例个数
    """
    global case_count
    case_count += 1
    return case_count

class _Exception(object):
    """异常类的封装"""
    def __init__(self, module, text=None):
        error = traceback.format_exc()
        if text is None:
            LOG.logging_debug(error)
            Driver.quit()
            print(RED_BIG, LoginError(module, error))
        else:
            LOG.logging_debug(text)
            Driver.quit()
            print(RED_BIG, LoginSelectError(module))

def _login_module(account=None, password=None, company=None, in_login=False, module=None):
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
                _Exception(module)
        else:
            _Exception(module)
    else:
        try:
            LoginTestModules(Driver).opens_if()
        except Exception:
            _Exception(module)

def setUpModule(currentModule):
    """模块初始化"""
    global Driver, SQL, Error, LOG, wait
    LOG = Logger()
    SQL = Mysql()
    Error = None
    wait = MyYaml('implicitly_wait').config
    Driver = browser(MyYaml('browser').config)
    account = MyYaml('account').config
    password = MyYaml('password').config
    company = MyYaml('company').config
    if isinstance(wait, int):
        Driver.set_page_load_timeout(wait * 2)
    else:
        raise WaitTypeError(FUN_NAME(os.path.dirname(__file__)))
    if 'ValidateLogin_st' not in currentModule:
        _login_module(in_login=True, account=account, password=password, company=company, module=currentModule)
    else:
        _login_module(in_login=False, module=currentModule)


def tearDownModule():
    """模块结束"""
    Driver.quit()
    SQL.close_sql()


class UnitTests(unittest.TestCase):
    global case_count
    # noinspection PyRedeclaration
    case_count = 0
    log = start_time = result = status = level = img = error  =  None
    first = second = author = urls =  None
    RE_LOGIN, LOGIN_INFO, MODULE = False, None, None

    @classmethod
    def setUpClass(cls):
        """判断类下面是否需要重新请求账号登录"""
        if cls.RE_LOGIN:
            account = cls.LOGIN_INFO["account"]
            password = cls.LOGIN_INFO["password"]
            company = cls.LOGIN_INFO.get("company")
            if account and password is not None:
                _login_module(in_login=True, account=account, password=password, company=company, module=cls.__class__)
            else:
                raise TypeError(LoginSelectError)

    @classmethod
    def tearDownClass(cls):
        """"""
        pass

    def setUp(self):
        """用例初始化"""
        self.driver = Driver
        self.sql = SQL
        self.setLog = Error
        self.count = _case_id()
        self.module = self.__class__.__module__
        self.class_name = self.__class__.__name__
        self.case_name = self._testMethodName
        self.current_path = os.path.dirname(__file__)
        _data_initialization = Get(module=self.MODULE, class_name=self.class_name, case_name=self.case_name)
        _return_data= _data_initialization.re()
        self.level = _return_data.get("level")
        self.author = _return_data.get("author")
        self.url = _return_data.get("url")
        self.second = _return_data.get("asserts")
        self.case_remark = _return_data.get("scene")
        if self.case_remark:
            self.data = _data_initialization.param_extract(self.case_remark)
        else:
            raise TypeError("common中scene参数为空，此参数不能为空，请增加")
        self.driver.set_page_load_timeout(wait)
        self.current_time = standard_time()
        self.screenshots_path = read_file('img', '{}.png'.format(self.case_name))
        if self.setLog is not None:
            LOG.logging_debug(LogErrors.format(self.current_time, self.current_path, self.setLog))
        self.start_time = time.time()

    def tearDown(self):
        """用例结束"""
        end_time = time.time()
        total_time = end_time - self.start_time
        warnings.filterwarnings('ignore')
        error_path = '{}/{}/{}'.format(self.module, self.class_name, self.case_name)
        MyAsserts(self.first, self.second, self.count, self.level, self.case_name, self.case_remark,
                                self.status, self.error, self.url, total_time, self.driver, self.class_name,
                                self.screenshots_path, self.author, self, error_path, LOG).asserts()

if __name__ == '__main__':
    unittest.main()
    y = 'dsds'
    print(y.encode().decode())