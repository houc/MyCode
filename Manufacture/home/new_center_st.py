import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.home.currency import HomeElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestNewCenter(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    
    def test_good_news_table_one(self):
        """
        验证GoodNews是否能正常打开并跳转;

        1、打开首页;

        2、点击GoodNews;

        3、断言跳转的url是否包含{/news/71.html}
        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.new_table_click(location=1)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.news_assert(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_good_news_table_two(self):
        """
        验证GoodNewsTwo是否能正常打开并跳转;

        1、打开首页;

        2、点击GoodNewsTwo;

        3、断言跳转的url是否包含{/news/48.html}
        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.new_table_click(location=2)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.news_assert(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_launching(self):
        """
        验证launching是否能正常打开并跳转;

        1、打开首页;

        2、点击launching;

        3、断言跳转的url是否包含{/news/47.html}
        """
        try:
            driver = HomeElement(self.driver)
            driver.get(self.url)
            driver.new_table_click(location=3)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.news_assert(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
