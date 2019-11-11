import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner, check_upper_is_ok
from model.SkipModule import Skip, current_module
from door_ui.test_debug.currency import TestDebugElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class Debug(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = False
    BROWSER = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up, retry_count=1)
    @check_upper_is_ok('test_all_5')
    def test_all(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        self.first = s
        self.assertEqual(self.first, self.second)
        
    @test_re_runner(set_up)
    @check_upper_is_ok('test_all_1')
    def test_all_2(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """

        # self.first = False
        self.assertEqual(self.first, self.second)
        
    @test_re_runner(set_up)
    # @case_self_monitor('test_all_3')
    def test_all_3(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        self.first = True
        self.assertEqual(self.first, self.second)
        
    @test_re_runner(set_up)
    def test_all_1(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        # driver = TestDebugElement(self.driver)
        # self.screenshots = driver.screen_base64_shot()
        self.assertEqual(self.first, self.second)
        
    @test_re_runner(set_up)
    @unittest.skip('暂跳')
    def test_all_5(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        driver = TestDebugElement(self.driver)
        driver.get(self.url)
        self.first = False
        self.screenshots = driver.screen_base64_shot()
        self.assertEqual(self.first, self.second)

    def test_all_4(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        print('!')
        self.assertEqual(self.first, self.second)
        
