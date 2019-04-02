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
class InModuleInfo(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_automotive_filter_series_info(self):
        """
        验证AutomotiveFilterSeries图片详情是否能正常跳转;

        1、打开AutomotiveFilterSeries;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/162.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_automotive_brake_info(self):
        """
        验证automotive_brake图片详情是否能正常跳转;

        1、打开automotive_brake;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/152.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_compressor_info(self):
        """
        验证Compressor图片详情是否能正常跳转;

        1、打开Compressor;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/145.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_seal_series_or_oil_seal_info(self):
        """
        验证seal_series_or_oil_seal图片详情是否能正常跳转;

        1、打开seal_series_or_oil_seal;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/139.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_motor_drain_valve_info(self):
        """
        验证motor_drain_valve图片详情是否能正常跳转;

        1、打开motor_drain_valve;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/138.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_shock_absorber_info(self):
        """
        验证shock_absorber图片详情是否能正常跳转;

        1、打开shock_absorber;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/137.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_rubber_miscellaneous_items_info(self):
        """
        验证rubber_miscellaneous_items图片详情是否能正常跳转;

        1、打开rubber_miscellaneous_items;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/135.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_general_rubber_parts_info(self):
        """
        验证general_rubber_parts图片详情是否能正常跳转;

        1、打开general_rubber_parts;

        2、点击第{1}张图片;

        3、断言跳转的url是否包含{/product/126.html}
        """
        try:
            driver = ProductsElement(self.driver)
            driver.get(self.url)
            driver.img_click(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1]) # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

