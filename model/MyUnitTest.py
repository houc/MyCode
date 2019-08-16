import unittest
import time
import os

from model.Logs import logger
from model.Yaml import MyConfig
from model.DriverParameter import browser
from model.MyAssert import MyAsserts
from model.GetYamlMessages import GetConfigMessage as Get
from model.MyException import LoginSelectError
from door_ui.common import LoginPublic


class UnitTests(unittest.TestCase):
    first = second = author = urls = login = driver = status = error = screenshots= None
    RE_LOGIN, LOGIN_INFO, MODULE, BROWSER = False, None, None, True

    @classmethod
    def setUpClass(cls):
        """判断类下面是否需要重新请求账号登录"""
        global module
        try:
            driver_headless = MyConfig('browser').config
            if cls.BROWSER:
                cls.driver = browser(switch=driver_headless)
                cls.driver.implicitly_wait(20)
                if cls.RE_LOGIN:
                    account = cls.LOGIN_INFO['account']
                    password = cls.LOGIN_INFO['password']
                    module = cls.MODULE.split('\\')[-1].split('.')[0]
                    if account and password:
                        cls.login = LoginPublic(driver=cls.driver, account=account,
                                    password=password,
                                    module=module)
                        cls.login.login_design()
                    else:
                        raise LoginSelectError(cls.MODULE.split('\\')[-1].split('.')[0])
        except Exception:
            if cls.BROWSER:
                cls.driver.quit()
            if cls.RE_LOGIN:
                cls.login.remove_token(keys=module)
            raise

    @classmethod
    def tearDownClass(cls):
        """清除配置文件中的token"""
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
        self.case_scene = _return_data['scene']
        self.case_remark = _return_data['case_remark']
        self.data = _data_initialization.param_extract(self.case_scene)
        self.start_time = time.time()
        return self.driver

    def tearDown(self):
        """用例结束"""
        end_time = time.time()
        total_time = end_time - self.start_time
        error_path = f'{self.catalog}/{self.case_name}'
        if self.BROWSER:
            log_br = self.driver.get_log('browser')
            log_dr = self.driver.get_log('driver')
            logger.debug(log_br)
            logger.debug(log_dr)
        MyAsserts(self.first, self.second, self.catalog, self.level, self.case_name, self.case_scene,
                  self.status, self.error, self.url, total_time, self.driver, self.assembly,
                  self.screenshots, self.author, self, error_path, logger,
                  case_remark=self.case_remark).asserts()
