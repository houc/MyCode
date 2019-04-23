import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from SCRM.login.currency import LoginElement
from SCRM.common import LoginPublic

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]

    def test_repeat_login_1(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_2(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_3(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_4(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_5(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_6(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_7(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_8(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_9(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_10(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_11(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_12(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_13(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_14(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_15(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_16(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_17(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_18(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_19(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_20(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_21(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_22(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_23(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_24(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_25(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_26(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_27(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_28(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_29(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_30(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_31(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_32(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_33(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_34(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_35(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_36(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_37(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_38(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_39(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_40(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_41(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_42(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_43(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_44(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_45(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_46(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_47(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_48(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_49(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_50(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_51(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_52(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_53(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_54(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_55(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_56(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_57(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_58(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_59(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_60(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_61(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_62(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_63(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_64(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_65(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_66(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_67(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_68(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_69(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_70(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_71(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_72(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_73(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_74(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_75(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_76(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_77(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_78(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_79(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_80(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_81(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_82(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_83(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_84(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_85(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_86(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_87(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_88(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_89(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_90(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_91(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_92(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_93(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_94(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_95(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_96(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_97(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_98(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_99(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_100(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_101(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_102(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_103(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_104(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_105(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_106(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_107(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_108(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_109(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_110(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_111(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_112(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_113(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_114(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_115(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_116(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_117(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_118(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_119(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_120(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_121(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_122(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_123(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_124(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_125(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_126(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_127(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_128(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_129(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_130(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_131(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_132(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_133(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_134(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_135(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_136(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_137(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_138(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_139(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_140(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_141(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_142(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_143(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_144(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_145(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_146(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_147(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_148(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_149(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_150(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_151(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_152(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_153(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_154(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_155(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_156(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_157(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_158(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_159(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_160(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_161(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_162(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_163(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_164(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_165(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_166(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_167(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_168(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_169(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_170(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_171(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_172(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_173(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_174(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_175(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_176(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_177(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_178(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_179(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_180(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_181(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_182(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_183(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_184(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_185(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_186(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_187(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_188(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_189(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_190(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_191(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_192(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_193(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_194(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_195(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_196(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_197(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_198(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_199(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_200(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_201(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_202(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_test_repeat_login_203(self):
        """
        测试循环登录，用例时长

        1、输入账号{15882223197}，输入密码{Po123456};

        2、点击登录;

        3、验证是否加载出邮件元素
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.F5()
            LoginPublic(self.driver, self.data[0], self.data[1], module=self.toke_module).login(False)
            self.first = driver.assert_mail()
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

