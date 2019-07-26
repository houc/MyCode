import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from SCRM.workbench.currency import WorkbenchElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestWorkResults(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": 15800000445, "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_send_ordinary_mail_exist(self):
        """
        登录首页验证{发送普通邮件}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.result_opera(1)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_send_mark_mail_exist(self):
        """
        登录首页验证{发送营销邮件}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.result_opera(2)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_received_mail_exist(self):
        """
        登录首页验证{收到邮件}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.result_opera(3)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_add_contact_exist(self):
        """
        登录首页验证{新增联系人}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.result_opera(4)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_add_customer_exist(self):
        """
        登录首页验证{新增客户}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.result_opera(5)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

