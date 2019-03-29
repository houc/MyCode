import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.news.currency import NewsElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestNewsTable(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_company_news(self):
        """
        验证CompanyNews是否能正常跳转;

        1、打开News;

        2、点击CompanyNews;

        3、断言跳转的url是否包含{/news/2/}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.news_table_click(location=1)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_industry_dynamics(self):
        """
        验证IndustryDynamics是否能正常跳转;

        1、打开News;

        2、点击IndustryDynamics;

        3、断言跳转的url是否包含{/news/3/}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.news_table_click(location=2)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_notice(self):
        """
        验证Notice是否能正常跳转;

        1、打开News;

        2、点击Notice;

        3、断言跳转的url是否包含{/news/4/}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.news_table_click(location=3)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_knowledge(self):
        """
        验证Knowledge是否能正常跳转;

        1、打开News;

        2、点击Knowledge;

        3、断言跳转的url是否包含{/news/5/}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.news_table_click(location=4)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_public_welfare(self):
        """
        验证PublicWelfare是否能正常跳转;

        1、打开News;

        2、点击PublicWelfare;

        3、断言跳转的url是否包含{/news/6/}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.news_table_click(location=5)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_news_center(self):
        """
        验证NewsCenter是否能正常跳转;

        1、打开News;

        2、点击NewsCenter中的第{1}条数据;

        3、断言跳转的url是否包含{/news/}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.news_info_click(location=self.data[0])
            driver.switch_windows(name=-1)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[1])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

    def test_news_center_next_page(self):
        """
        验证NewsCenter点击下一页是否正常跳转;

        1、打开News;

        2、点击NewsCenter;

        3、点击下一页;

        4、断言跳转的url是否包含{/nav/10.html#c_news_list-15487307331178472}
        """
        try:
            driver = NewsElement(self.driver)
            driver.get(self.url)
            driver.next_page_click()
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.is_asserts = True # 断言self.first与self.second是否相等, True:相等，False:不相等
        except Exception as exc:
            self.error = str(exc)

