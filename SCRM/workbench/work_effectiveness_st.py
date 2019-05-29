import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from SCRM.workbench.currency import WorkbenchElement
from model.TimeConversion import compact_time

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class WorkEffectiveness(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15928564313', "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]

    @unittest.skip('创建邮件后，延迟比较严重..')
    def test_send_ordinary_mail(self):
        """
        验证发送普通邮件后，工作台【发送普通邮件】是否会+1

        1、点击{新建邮件}；

        2、收件人输入{1063116271@qq.com}；

        3、主题输入{自动化测试}；

        4、点击【发送】；

        5、刷新浏览器查看是否+1
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            time.sleep(5)
            self.first = driver.work_num(location=1)
            driver.quick_button(self.data[0])
            driver.add_mail(addressee=self.data[1], theme=self.data[2])
            time.sleep(1)
            driver.send_button()
            time.sleep(5)
            driver.F5()
            time.sleep(5)
            self.second = driver.work_num(location=1)
            self.screenshots = driver.screen_base64_shot()
            self.assertNotEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_create_contacts(self):
        """
        验证新增联系人后，工作台【新增联系人】是否会+1

        1、点击{新增联系人}并提示{联系人已成功创建};

        2、输入邮箱地址{%d@qq.com};

        3、点击【保存】;

        4、刷新浏览器查看是否+1
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            time.sleep(5)
            self.second = driver.work_num(location=4)
            driver.quick_button(self.data[0])
            driver.add_contacts(input_location=1, mail=compact_time() + '@qq.com')
            time.sleep(1)
            driver.save(location=4)
            driver.save(location=4)
            message = driver.message_top_box()
            self.assertEqual(message, self.data[1])
            driver.F5()
            time.sleep(5)
            self.first = driver.work_num(location=4)
            self.screenshots = driver.screen_base64_shot()
            self.assertNotEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_create_customer(self):
        """
        验证新增客户后，工作台【新增客户】是否会+1

        1、点击{新增客户}并提示{保存成功！};

        2、输入国家选择{中国};

        3、输入{测试客户}后，点击【保存】;

        4、刷新浏览器查看是否+1
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            time.sleep(5)
            self.second = driver.work_num(location=5)
            driver.quick_button(self.data[0])
            driver.add_customer(china=self.data[2], location=2, customer=self.data[3])
            driver.save(location=4, wait=2)
            message = driver.message_top_box()
            self.assertEqual(message, self.data[1])
            driver.F5()
            time.sleep(5)
            self.first = driver.work_num(location=5)
            self.screenshots = driver.screen_base64_shot()
            self.assertNotEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

