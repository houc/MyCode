import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.technology.currency import TechnologyElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestTechnologyTable(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    
    def test_switch_download(self):
        """
        验证Download是否能正常跳转;

        1、打开Technology;

        2、点击Download;

        3、断言跳转的url是否包含{/news/8/}
        """
        try:
            driver = TechnologyElement(self.driver)
            driver.get(self.url)
            driver.technology_table_click(location=1)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_switch_equipment(self):
        """
        验证Equipment是否能正常跳转;

        1、打开Technology;

        2、点击Equipment;

        3、断言跳转的url是否包含{/news/9/}
        """
        try:
            driver = TechnologyElement(self.driver)
            driver.get(self.url)
            driver.technology_table_click(location=2)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_technology_info(self):
        """
        验证Technology图片新闻是否能进入详情并跳转;

        1、打开Technology;

        2、点击第{1}张新闻图片;

        3、断言跳转的url是否包含{/news/70.html}
        """
        try:
            driver = TechnologyElement(self.driver)
            driver.get(self.url)
            driver.img_info(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_equipment_info(self):
        """
        验证Equipment图片新闻是否能进入详情并跳转;

        1、打开Equipment;

        2、点击第{1}张新闻图片;

        3、断言跳转的url是否包含{/news/62.html}
        """
        try:
            driver = TechnologyElement(self.driver)
            driver.get(self.url)
            driver.img_info(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_download_info(self):
        """
        验证Download图片新闻是否能进入详情并跳转;

        1、打开Download;

        2、点击第{1}张新闻图片;

        3、断言跳转的url是否包含{/news/24.html}
        """
        try:
            driver = TechnologyElement(self.driver)
            driver.get(self.url)
            driver.img_info(location=self.data[0])
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_switch_technology(self):
        """
        验证Technology是否能正常跳转;

        1、打开Technology;

        2、点击Technology;

        3、断言跳转的url是否包含{/news/10/}
        """
        try:
            driver = TechnologyElement(self.driver)
            driver.get(self.url)
            driver.technology_table_click(location=3)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_equal(url=self.data[0]) # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

