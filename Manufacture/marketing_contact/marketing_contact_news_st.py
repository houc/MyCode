import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.marketing_contact.currency import MarketingContactElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestMarketingContactNews(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    
    def test_market_contact_news(self):
        """
        验证marketing页跳转页末news页
        1、打开首页;

        2、点击marketing;

        3、点击页末news;

        4、断言跳转的url是否包含{/nav/58.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contect_companyNews(self):
        """
        验证marketing页跳转页末companyNews页
        1、打开首页;

        2、点击marketing;

        3、点击页末companyNews;

        4、断言跳转的url是否包含{/nav/59.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contect_industryDynamics(self):
        """
        验证marketing页跳转页末industryDynamics页
        1、打开首页;

        2、点击marketing;

        3、点击页末industryDynamics;

        4、断言跳转的url是否包含{/nav/60.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contect_notice(self):
        """
        验证marketing页跳转页末notice页
        1、打开首页;

        2、点击marketing;

        3、点击页末notice;

        4、断言跳转的url是否包含{/nav/61.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_knowledge(self):
        """
        验证marketing页跳转页末knowledge页
        1、打开首页;

        2、点击marketing;

        3、点击页末knowledge;

        4、断言跳转的url是否包含{/nav/62.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_publicWelfare(self):
        """
        验证marketing页跳转页末publicWelfare页
        1、打开首页;

        2、点击marketing;

        3、点击页末publicWelfare;

        4、断言跳转的url是否包含{/nav/63.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

