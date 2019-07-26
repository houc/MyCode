import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from SCRM.data_report_from.currency import DataReportFromElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestCustomerReport(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": 15800000450, "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_30_day1(self):
        """
        统计时间“近30天”是否存在
        """
        try:
            driver = DataReportFromElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.time_switch(2)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_3_moth1(self):
        """
        统计时间“近3个月”是否存在
        """
        try:
            driver = DataReportFromElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.time_switch(3)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_half_year1(self):
        """
        统计时间“近半年”是否存在
        """
        try:
            driver = DataReportFromElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.time_switch(4)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_1_year1(self):
        """
        统计时间“近一年”是否存在
        """
        try:
            driver = DataReportFromElement(self.driver)
            driver.get(self.url)
            time.sleep(2)
            self.first = driver.time_switch(5)
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

