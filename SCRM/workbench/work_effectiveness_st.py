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
class WorkEffectiveness(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15928564313', "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    
    def test_send_ordinary_mail(self):
        """
        验证发送普通邮件后，工作台【发送普通邮件】是否会+1

        1、点击{新建邮件}；

        2、收件人输入{1063116271@qq.com}；

        3、主题输入{自动化测试}；

        4、点击{发送}；

        5、刷新浏览器查看是否+1
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.work_num(location=1)
            driver.quick_button(self.data[0])
            driver.add_mail(addressee=self.data[1], theme=self.data[2])
            time.sleep(2)
            driver.F5()
            self.second = driver.work_num(location=1)
            driver.screen_shot(self.screenshots_path)
            self.assertNotEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

