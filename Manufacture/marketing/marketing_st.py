import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.marketing.currency import MarketingElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestMarketing(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    
    def test_market(self):
        """
        验证marketing是否能正常打开;

        1、打开首页;

        2、点击marketing;

        3、断言跳转的url是否包含{/nav/13.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            time.sleep(5)
            driver.market_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_concept(self):
        """
        验证marketing页中concept页签是否能正常打开;

        1、打开首页;

        2、点击marketing;

        3、点击Concept;

        4、断言跳转的url是否包含{/intro/10.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            driver.market_click()
            driver.concept_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_network(self):
        """
        验证marketing页中concept页签是否能正常打开;

        1、打开首页;

        2、点击marketing;

        3、点击Network;

        4、断言跳转的url是否包含{/intro/11.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            driver.market_click()
            driver.network_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_market_marketing_knowledge(self):
        """
        验证marketing页中concept页签是否能正常打开;

        1、打开首页;

        2、点击marketing;

        3、点击Marketing
        knowledge;

        4、断言跳转的url是否包含{/intro/12.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            driver.market_click()
            driver.marketing_knowledge_click()
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    @unittest.skip('暂时跳过A')
    def test_market_home(self):
        """
        验证marketing页跳转表头home页;

        1、打开首页;

        2、点击marketing;

        3、点击home;

        4、断言跳转的url是否包含{/nav/1.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            # 操作元素.....

            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = ""  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    @unittest.skip('暂时跳过B')
    def test_market_about(self):
        """
        验证marketing页跳转表头about页;

        1、打开首页;

        2、点击marketing;

        3、点击about;

        4、断言跳转的url是否包含{/nav/2.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            # 操作元素.....

            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = ""  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    @unittest.skip('暂时跳过C')
    def test_market_news(self):
        """
        验证marketing页跳转表头news页;

        1、打开首页;

        2、点击marketing;

        3、点击news;

        4、断言跳转的url是否包含{/nav/10.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            # 操作元素.....

            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = ""  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    @unittest.skip('暂时跳过D')
    def test_market_product(self):
        """
        验证marketing页跳转表头product页;

        1、打开首页;

        2、点击marketing;

        3、点击product;

        4、断言跳转的url是否包含{/nav/11.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            # 操作元素.....

            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = ""  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    @unittest.skip('暂时跳过E')
    def test_market_technology(self):
        """
        验证marketing页跳转表头technology页;

        1、打开首页;

        2、点击marketing;

        3、点击technology;

        4、断言跳转的url是否包含{/nav/12.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            # 操作元素.....

            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = ""  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    @unittest.skip('暂时跳过F')
    def test_market_contact(self):
        """
        验证marketing页跳转表头contact页;

        1、打开首页;

        2、点击marketing;

        3、点击contact;

        4、断言跳转的url是否包含{/nav/24.html}
        """
        try:
            driver = MarketingElement(self.driver)
            driver.get(self.url)
            # 操作元素.....

            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = ""  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

