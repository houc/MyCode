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
class TestMarketingContactProducts(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_market_contact_products(self):
        """
        验证marketing页跳转页末Products页
        1、打开首页;

        2、点击marketing;

        3、点击页末Products;

        4、断言跳转的url是否包含{/nav/72.html}
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

    def test_market_contact_automoticeFilterSeries(self):
        """
        验证marketing页跳转页末automoticeFilterSeries页
        1、打开首页;

        2、点击marketing;

        3、点击页末automoticeFilterSeries;

        4、断言跳转的url是否包含{/nav/74.html}
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

    def test_market_contact_automotiveBrake(self):
        """
        验证marketing页跳转页末automotiveBrake页
        1、打开首页;

        2、点击marketing;

        3、点击页末automotiveBrake;

        4、断言跳转的url是否包含{/nav/75.html}
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

    def test_market_contact_compressor(self):
        """
        验证marketing页跳转页末compressor页
        1、打开首页;

        2、点击marketing;

        3、点击页末compressor;

        4、断言跳转的url是否包含{/nav/76.html}
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

    def test_market_contact_sealSeriesOilSeal(self):
        """
        验证marketing页跳转页末sealSeriesOilSeal页
        1、打开首页;

        2、点击marketing;

        3、点击页末sealSeriesOilSeal;

        4、断言跳转的url是否包含{/nav/77.html}
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

    def test_market_contact_motorDrainValue(self):
        """
        验证marketing页跳转页末motorDrainValue页
        1、打开首页;

        2、点击marketing;

        3、点击页末motorDrainValue;

        4、断言跳转的url是否包含{/nav/78.html}
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

    def test_market_contact_shockAbsorber(self):
        """
        验证marketing页跳转页末shockAbsorber页
        1、打开首页;

        2、点击marketing;

        3、点击页末shockAbsorber;

        4、断言跳转的url是否包含{/nav/79.html}
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

    def test_market_contact_rubberMiscellaneousItems(self):
        """
        验证marketing页跳转页末rubberMiscellaneousItems页
        1、打开首页;

        2、点击marketing;

        3、点击页末rubberMiscellaneousItems;

        4、断言跳转的url是否包含{/nav/80.html}
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

    def test_market_contact_generalRubberParts(self):
        """
        验证marketing页跳转页末generalRubberParts页
        1、打开首页;

        2、点击marketing;

        3、点击页末generalRubberParts;

        4、断言跳转的url是否包含{/nav/81.html}
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

