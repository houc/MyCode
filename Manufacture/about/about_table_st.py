import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from Manufacture.about.currency import AboutElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestAboutUs(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_profile(self):
        """
        验证Profile是否能正常打开并跳转;

        1、打开About;

        2、点击Profile;

        3、断言跳转的url是否包含{/intro/1.html}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=1)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_speech(self):
        """
        验证Speech是否能正常打开并跳转;

        1、打开About;

        2、点击Speech;

        3、断言跳转的url是否包含{/intro/3.html}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=2)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_organization(self):
        """
        验证Organization是否能正常打开并跳转;

        1、打开About;

        2、点击Organization;

        3、断言跳转的url是否包含{/intro/4.html}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=3)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_philosophy(self):
        """
        验证Philosophy是否能正常打开并跳转;

        1、打开About;

        2、点击Philosophy;

        3、断言跳转的url是否包含{/intro/6.html}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=4)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_honor(self):
        """
        验证Honor是否能正常打开并跳转;

        1、打开About;

        2、点击Honor;

        3、断言跳转的url是否包含{/honor.html?atlasCateId=1}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=5)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_staff_style(self):
        """
        验证StaffStyle是否能正常打开并跳转;

        1、打开About;

        2、点击StaffStyle;

        3、断言跳转的url是否包含{/honor.html?atlasCateId=2}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=6)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_honor_next_page(self):
        """
        验证Honor点击下一页是否能正常跳转;

        1、打开About;

        2、点击Honor;

        3、点击下一页;

        4、断言下一页跳转的url是否包含{/honor.html?atlasCateId=1#c_atlas_list-15487240148372429}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=5)
            driver.about_next_click_page()
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_staff_style_next_page(self):
        """
        验证StaffStyle点击下一页是否能正常跳转;

        1、打开About;

        2、点击StaffStyle;

        3、点击下一页;

        4、断言下一页跳转的url是否包含{/honor.html?atlasCateId=2#c_atlas_list-15487240148372429}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=6)
            driver.about_next_click_page()
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[0])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_honor_img(self):
        """
        验证Honor点击图片是否能正常跳转;

        1、打开About;

        2、点击Honor;

        3、点击第{1}张图片;

        4、断言下一页跳转的url是否包含{/atlas/}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=5)
            driver.img_click(location=self.data[0])
            driver.switch_windows(name=-1)
            driver.full_windows_screen(self.screenshots_path)
            self.first = driver.is_url_contain(url=self.data[1])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_staff_style_img(self):
        """
        验证StaffStyle点击图片是否能正常跳转;

        1、打开About;

        2、点击StaffStyle;

        3、点击第{1}张图片;

        4、断言下一页跳转的url是否包含{/atlas/}
        """
        try:
            driver = AboutElement(self.driver)
            driver.get(self.url)
            driver.about_table_click(location=6)
            driver.img_click(location=self.data[0])
            driver.switch_windows(name=-1)
            driver.full_windows_screen(self.screenshots_path, 1920, 980)
            self.first = driver.is_url_contain(url=self.data[1])  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

