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
_SKIP = True


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestQuick(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": 15800000444, "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_email_is_exist(self):
        """
        登录首页验证{新建邮件}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.opera_quick(1)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_task_is_exist(self):
        """
        登录首页验证{新建任务}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.opera_quick(2)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_task_is_contact(self):
        """
        登录首页验证{新建联系人}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.opera_quick(3)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_task_is_customer(self):
        """
        登录首页验证{新建客户}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.opera_quick(4)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_task_is_mark_mail(self):
        """
        登录首页验证{新建营销邮件}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.opera_quick(5)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_task_is_mark_mail_process(self):
        """
        登录首页验证{新建营销邮件流程}是否存在
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.opera_quick(6)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

