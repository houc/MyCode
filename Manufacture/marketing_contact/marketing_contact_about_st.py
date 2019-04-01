import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.marketing_contact.currency import MarketingContactElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestMarketingContactAbout(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_market_contact_about(self):
        """
        验证marketing页跳转页末about页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末about;

        4、断言跳转的url是否包含{/nav/51.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_profile(self):
        """
        验证marketing页跳转页末profile页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末profile;

        4、断言跳转的url是否包含{/nav/52.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_speech(self):
        """
        验证marketing页跳转页末speech页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末speech;

        4、断言跳转的url是否包含{/nav/53.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_organization(self):
        """
        验证marketing页跳转页末organization页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末organization;

        4、断言跳转的url是否包含{/nav/54.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_system(self):
        """
        验证marketing页跳转页末system页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末system;

        4、断言跳转的url是否包含{/nav/55.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_philosophy(self):
        """
        验证marketing页跳转页末philosophy页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末philosophy;

        4、断言跳转的url是否包含{/nav/56.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_honor(self):
        """
        验证marketing页跳转页末honor页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末honor;

        4、断言跳转的url是否包含{/nav/57.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_contact_about_stafStyle(self):
        """
        验证marketing页跳转页末stafStyle页是否正常;

        1、打开首页;

        2、点击marketing;

        3、点击页末stafStyle;

        4、断言跳转的url是否包含{/nav/70.html}
        """
        try:
            driver = MarketingContactElement(self.driver)
            driver.get(self.url)
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

