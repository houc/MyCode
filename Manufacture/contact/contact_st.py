import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.contact.currency import ContactElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestContact(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    
    def test_contact(self):
        """
        验证首页顶部CONTACT是否能正常跳转;

        1、打开home;

        2、点击顶部导航栏Contact;

        3、断言跳转的url是否包含{/nav/24.html}
        """
        try:
            driver = ContactElement(self.driver)
            driver.get(self.url)
            driver.contact_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_ContactUs(self):
        """
        验证首页顶部CONTACT US是否能正常跳转;

        1、打开Contact;

        2、点击导航栏Contact us;

        3、断言跳转的url是否包含{/intro/13.html}
        """
        try:
            driver = ContactElement(self.driver)
            driver.get(self.url)
            # 操作元素.....
            driver.contacts_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_Message(self):
        """
        验证首页顶部CONTACT
        US是否能正常跳转;

        1、打开Contact;

        2、点击导航栏Message;

        3、断言跳转的url是否包含{/messages.html}
        """
        try:
            driver = ContactElement(self.driver)
            driver.get(self.url)
            driver.message_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)
