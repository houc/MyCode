import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from SCRM.workbench.currency import WorkbenchElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class ShortcutFunction(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15800000444', "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]

    def test_create_mail(self):
        """
        验证新建邮件快捷功能是否能正常跳转

        1、点击{新建邮件};
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            self.first = driver.text_mail(location=1)
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_create_task(self):
        """
        验证新增任务快捷功能是否能正常跳转

        1、点击{新增任务};
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            self.first = driver.text_mail(location=1)
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
            driver.cancel_button(location=1)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_quick_create_contacts(self):
        """
        验证新增联系人快捷功能是否能正常跳转

        1、点击{新增联系人};
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            self.first = driver.text_mail(location=1)
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_quick_create_customer(self):
        """
        验证新增客户快捷功能是否能正常跳转

        1、点击{新增客户};
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            self.first = driver.text_mail(location=2)
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_quick_create_marketing(self):
        """
        验证新增营销邮件快捷功能是否能正常跳转

        1、点击{新建营销邮件};
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            self.first = driver.is_url_contain(url=self.data[1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_marketing_standard(self):
        """
        验证新建营销邮件流程标准快捷功能是否能正常跳转

        1、点击{新建营销邮件流程};

        2、选择{标准}，点击{确定};

        3、验证跳转的URL是否包含{/flow/flow_new?type=1}
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            driver.process_click()
            self.first = driver.is_url_contain(url=self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_marketing_fixed(self):
        """
        验证新建营销邮件流程固定日期快捷功能是否能正常跳转

        1、点击{新建营销邮件流程};

        2、选择{固定日期型}，点击{确定};

        3、验证跳转的URL是否包含{/flow/flow_new?type=2&value=}
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            driver.marketing_type(text=self.data[1])
            driver.process_click()
            self.first = driver.is_url_contain(url=self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_marketing_week(self):
        """
        验证新建营销邮件流程周期快捷功能是否能正常跳转

        1、点击{新建营销邮件流程};

        2、选择{周期型}，选择{生日}，点击{确定};

        3、验证跳转的URL是否包含{/flow_new?type=3&value=birth_day}
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.F5()
            driver.quick_button(text=self.data[0])
            driver.marketing_type(text=self.data[1])
            driver.week_type(type=self.data[2])
            driver.process_click()
            self.first = driver.is_url_contain(url=self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

