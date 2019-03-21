import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from SCRM.login.currency import LoginElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_accountError(self):
        """
        验证错误的用户名进行登录:

        1、用户名输入框输入:{15928564314999};

        2、密码输入框输入:{Li123456};

        3、点击【登录】。
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.login_param(self.data[0], self.data[1])
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.assert_login(value="账号未注册")  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_passwordError(self):
        """
        验证错误的密码登录:

        1、用户名输入框输入:{15928564313};

        2、密码输入框输入:{Li1234564444};

        3、点击【登录】。
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.login_param(self.data[0], self.data[1])
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.assert_login(value="密码错误请重新输入")  # 此项为必填，第一个断言值
        except Exception as exc:
            self.error = str(exc)

    def test_accountNull(self):
        """
        验证用户名为空格登录:

        1、用户名输入框输入:{
        };

        2、密码输入框输入:{Li123456};

        3、点击【登录】。
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.login_param(self.data[0], self.data[1])
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.assert_login(value="请输入账号")  # 此项为必填，第一个断言值
        except Exception as exc:
            self.error = str(exc)

    def test_passwordNull(self):
        """
        验证密码为空格登录:

        1、用户名输入框输入:{15928564313};

        2、密码输入框输入:{
        };

        3、点击【登录】。
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.login_param(self.data[0], self.data[1])
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.assert_login(value="请输入密码")  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_passwordEnglish(self):
        """
        验证密码为全英文字节登录:

        1、用户名输入框输入:{15928564313};

        2、密码输入框输入:{AAVDVDVD23325GDFGDFG~!@#$%^&*()_};

        3、点击【登录】。
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.login_param(self.data[0], self.data[1])
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.assert_login(value="密码错误请重新输入")  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    @unittest.skip('暂时跳过该用例，调试困难')
    def test_success(self):
        """
        验证账号密码正确:

        1、用户名输入框输入:{15928564313};

        2、密码输入框输入:{Li123456};

        3、点击【登录】。
        """
        try:
            driver = LoginElement(self.driver)
            driver.get(self.url)
            driver.login_param(self.data[0], self.data[1])
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.success_assert(value="超人")  # 此项为必填，第一个断言值
        except Exception as exc:
            self.error = str(exc)

if __name__ == '__main__':
    unittest.main()