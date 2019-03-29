import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.home.currency import HomeElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestHome(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_about_us(self):
        """
        验证aboutUs是否能正常打开;

        1、打开首页;

        2、点击AboutUs;

        3、断言跳转的url是否包含{/nav/2.html}

        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=1)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)


    def test_product_center(self):
        """
        验证ProductsCenter是否能正常打开;

        1、打开首页;

        2、点击ProductsCenter;

        3、断言跳转的url是否包含{/nav/11.html}
        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=2)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_technological_strength(self):
        """
        验证TechnologicalStrength是否能正常打开;

        1、打开首页;

        2、点击TechnologicalStrength;

        3、断言跳转的url是否包含{/nav/12.html}
        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=3)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_contact_us(self):
        """
        验证ContactUs是否能正常打开;

        1、打开首页;

        2、点击ContactUs;

        3、断言跳转的url是否包含{/nav/24.html}
        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=4)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)
