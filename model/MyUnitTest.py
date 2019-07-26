import unittest
import time
import os

from model.Logs import logger
from model.Yaml import MyConfig
from model.DriverParameter import browser
from model.MyAssert import MyAsserts
from model.GetYamlMessages import GetConfigMessage as Get
from model.TimeConversion import standard_time
from model.MyException import LoginSelectError
from SCRM.common import LoginPublic


class UnitTests(unittest.TestCase):
    first = second = author = urls = login = driver = status = error = screenshots= None
    RE_LOGIN, LOGIN_INFO, MODULE, BROWSER = False, None, None, True

    @classmethod
    def setUpClass(cls):
        """判断类下面是否需要重新请求账号登录"""
        try:
            driver_headless = MyConfig('browser').config
            if cls.BROWSER:
                cls.driver = browser(switch=driver_headless)
                cls.driver.implicitly_wait(10)
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
        except Exception:
            try:
                cls.login.remove_key()
            except BaseException:
                pass
            if cls.BROWSER:
                cls.driver.quit()
            raise

    @classmethod
    def tearDownClass(cls):
        """清除配置文件中的token"""
        if cls.login is not None:
            cls.login.remove_key()
        if cls.BROWSER:
            cls.driver.quit()

    def setUp(self):
        """用例初始化"""
        self.class_name = self.__class__.__name__
        self.case_name = self._testMethodName
        self.current_path = os.path.dirname(__file__)
        self.catalog = self.__class__.__module__ + '.' + self.__class__.__name__
        _data_initialization = Get(module=self.MODULE.split('\\')[-2],
                                   class_name=self.class_name, case_name=self.case_name)
        _return_data= _data_initialization.re()
        self.level = _return_data['level']
        self.author = _return_data['author']
        self.url = _return_data['url']
        self.assembly = _return_data['assembly']
        self.second = _return_data['asserts']
        self.case_remark = _return_data['scene']
        self.data = _data_initialization.param_extract(self.case_remark)
        self.current_time = standard_time()
        self.start_time = time.time()
        return self.driver

    def tearDown(self):
        """用例结束"""
        end_time = time.time()
        total_time = end_time - self.start_time
        error_path = '{}/{}'.format(self.catalog, self.case_name)
        MyAsserts(self.first, self.second, self.catalog, self.level, self.case_name, self.case_remark,
                  self.status, self.error, self.url, total_time, self.driver, self.assembly,
                  self.screenshots, self.author, self, error_path, logger).asserts()
