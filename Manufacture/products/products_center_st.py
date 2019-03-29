import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.products.currency import ProductsElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestProductsCenterTable(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_automotive_filter_series(self):
        """
        验证AutomotiveFilterSeries是否能正常跳转;

        1、打开Products;

        2、点击AutomotiveFilterSeries;

        3、断言跳转的url是否包含{/product/5/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=1)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_automotive_brake(self):
        """
        验证AutomotiveBrake是否能正常跳转;

        1、打开Products;

        2、点击AutomotiveBrake;

        3、断言跳转的url是否包含{/product/7/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=2)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_compressor(self):
        """
        验证Compressor是否能正常跳转;

        1、打开Products;

        2、点击Compressor;

        3、断言跳转的url是否包含{/product/8/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=3)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_seal_series_or_oil_seal(self):
        """
        验证SealSeriesOilSeal是否能正常跳转;

        1、打开Products;

        2、点击SealSeriesOilSeal;

        3、断言跳转的url是否包含{/product/9/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=4)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_motor_drain_valve(self):
        """
        验证MotorDrainValve是否能正常跳转;

        1、打开Products;

        2、点击MotorDrainValve;

        3、断言跳转的url是否包含{/product/10/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=5)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_shock_absorber(self):
        """
        验证ShockAbsorber是否能正常跳转;

        1、打开Products;

        2、点击ShockAbsorber;

        3、断言跳转的url是否包含{/product/11/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=6)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_rubber_miscellaneous_items(self):
        """
        验证RubberMiscellaneousItems是否能正常跳转;

        1、打开Products;

        2、点击RubberMiscellaneousItems;

        3、断言跳转的url是否包含{/product/12/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=7)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_general_rubber_parts(self):
        """
        验证GeneralRubberParts是否能正常跳转;

        1、打开Products;

        2、点击GeneralRubberParts;

        3、断言跳转的url是否包含{/product/13/}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.table_click(location=8)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

