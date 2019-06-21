import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseHandle import CaseRunning
from model.SkipModule import Skip, current_module
from SCRM.report_test.currency import ReportTestElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestCheckErrors(UnitTests):
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

    @CaseRunning(set_up)
    def test_error_1(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_2(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_3(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_4(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_5(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_6(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_7(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_8(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_9(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_10(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_11(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_12(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_13(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_14(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_15(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_16(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_error_17(self):
        """
        错误校验
        """
        try:
            self.first = __slots__
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

