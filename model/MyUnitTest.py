import unittest
import warnings
import time
import os

from model.Logs import Logger
from model.Yaml import MyConfig
from model.MyDB import MyDB
from model.DriverParameter import browser
from model.MyAssert import MyAsserts
from model.GetYamlMessages import GetConfigMessage as Get
from model.TimeConversion import standard_time
from model.MyException import LoginSelectError
from config_path.path_file import read_file
from Manufacture.common import LoginPublic


class UnitTests(unittest.TestCase):
    first = second = author = urls = login = driver = status = error = None
    RE_LOGIN, LOGIN_INFO, MODULE = False, None, None

    @classmethod
    def setUpClass(cls):
        """判断类下面是否需要重新请求账号登录"""
        cls.driver = browser(switch=MyConfig('browser').config)
        cls.wait = MyConfig('page_loading_wait').config
        cls.sql = MyDB()
        cls.log = Logger()
        if cls.RE_LOGIN:
            account = cls.LOGIN_INFO['account']
            password = cls.LOGIN_INFO['password']
            company = cls.LOGIN_INFO['company']
            if account and password:
                cls.login = LoginPublic(driver=cls.driver, account=account,
                            password=password, company=company,
                            module=cls.MODULE.split('\\')[-1].split('.')[0])
                cls.login.login()
            else:
                raise LoginSelectError(cls.MODULE.split('\\')[-1].split('.')[0])

    @classmethod
    def tearDownClass(cls):
        """清除配置文件中的token"""
        if cls.login is not None:
            cls.login.remove_key()
        cls.driver.quit()

    def setUp(self):
        """用例初始化"""
        self.module = self.__class__.__module__
        self.class_name = self.__class__.__name__
        self.case_name = self._testMethodName
        self.current_path = os.path.dirname(__file__)
        _data_initialization = Get(module=self.MODULE.split('\\')[-2],
                                   class_name=self.class_name, case_name=self.case_name)
        _return_data= _data_initialization.re()
        self.level = _return_data.get('level')
        self.author = _return_data.get('author')
        self.url = _return_data.get('url')
        self.second = _return_data.get('asserts')
        self.case_remark = _return_data.get('scene')
        if self.case_remark:
            self.data = _data_initialization.param_extract(self.case_remark)
        else:
            msg = "{}.{}.{}".format(self.module, self.class_name, self.case_name)
            warnings.warn(msg + "common中scene参数为空，此参数不能为空，请增加")
        self.driver.set_page_load_timeout(self.wait)
        self.driver.set_script_timeout(self.wait)
        self.current_time = standard_time()
        self.screenshots_path = read_file('img', '{}.png'.format(self.case_name))
        self.start_time = time.time()

    def tearDown(self):
        """用例结束"""
        end_time = time.time()
        total_time = end_time - self.start_time
        error_path = '{}/{}/{}'.format(self.module, self.class_name, self.case_name)
        MyAsserts(self.first, self.second, self.module, self.level, self.case_name, self.case_remark,
                  self.status, self.error, self.url, total_time, self.driver, self.class_name,
                  self.screenshots_path, self.author, self, error_path, self.log).asserts()
