import unittest
import time

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestLogin(UnitTests):
    """
    当RE_LOGIN = True即为需要重新登录，或者是需要切换账号登录，当RE_LOGIN为True时，需要将LOGIN_INFO的value值全填写完成，否则会报错...
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    
    def test_accountError(self):
        """
        验证错误的用户名进行登录:
        1、用户名输入框输入:15928564314999;
        2、密码输入框输入:Li123456;
        3、点击【登录】。
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            self.second = '账号未注册'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "15928564314999")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "Li123456")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.XPATH("//*[text()='账号未注册']/..!!text")
        except Exception as exc:
            self.error = str(exc)

    def test_passwordError(self):
        """
        验证错误的密码登录:
        1、用户名输入框输入:15928564313;
        2、密码输入框输入:Li1234564444;
        3、点击【登录】。
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            self.second = '密码错误请重新输入'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "15928564313")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "Li1234564444")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.XPATH("//*[text()='密码错误请重新输入']/..!!text")
        except Exception as exc:
            self.error = str(exc)

    def test_accountNull(self):
        """
        验证用户名为空格登录:
        1、用户名输入框输入:
        ;
        2、密码输入框输入:Li1234564444;
        3、点击【登录】。
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            self.second = '请输入账号'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "  ")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "Li1234564444")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.XPATH("//*[text()='请输入账号']/..!!text")
        except Exception as exc:
            self.error = str(exc)

    def test_passwordNull(self):
        """
        验证密码为空格登录:
        1、用户名输入框输入:
        15928564313;
        2、密码输入框输入:
        
        ;
        3、点击【登录】。
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            self.second = '请输入密码'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "15928564313")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "  ")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.XPATH("//*[text()='请输入密码']/..!!text")
        except Exception as exc:
            self.error = str(exc)

    def test_passwordEnglish(self):
        """
        验证密码为全英文字节登录:
        1、用户名输入框输入:
        15928564313;
        2、密码输入框输入:
        
        ASDSDSFDSFDSFSDCSDCDSFCDSFDSFDSGDSGDSGDSFGDSFSDFSD;
        3、点击【登录】。
        """
        try:
            self.level = '低'
            self.author = '后超'
            self.urls = '/platform/#/account/login'
            self.second = '密码错误请重新输入'
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!click")
            driver.XPATH("//*[text()='手机号/邮箱']/../div[1]/input!!send", "15928564313")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!click")
            driver.XPATH("//*[text()='密码']/../div[1]/input!!send", "ASDSDSFDSFDSFSDCSDCDSFCDSFDSFDSGDSGDSGDSFGDSFSDFSD")
            driver.XPATH("//*[text()='登录']/..!!click")
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.XPATH("//*[text()='密码错误请重新输入']/..!!text")
        except Exception as exc:
            self.error = str(exc)

