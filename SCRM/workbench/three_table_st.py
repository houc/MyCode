import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from model.CaseHandle import CaseRunning
from SCRM.workbench.currency import WorkbenchElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class ThreeTable(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15800000445', "password": 'Li123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]

    set_up = UnitTests.setUp

    @CaseRunning(set_up)
    def test_mail_star(self):
        """
        验证星标邮件是否成功

        1、选择第{1}条邮件;

        2、点击星标
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            driver.mark_star_mail()
            self.first = driver.message_top_box()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @CaseRunning(set_up)
    def test_today_task(self):
        """
        验证新增任务后今日任务统计是否+1

        1、点击{新增任务};

        2、任务主题输入{测试任务主题};

        3、负责人选择当前登录的人员;

        4、点击【确定】，刷新浏览器
        """
        try:
            driver = WorkbenchElement(self.driver)
            driver.get(self.url)
            self.first = driver.get_table_text()
            driver.quick_button(self.data[0])
            driver.add_task(self.data[1])
            message = driver.message_top_box()
            self.assertEqual(message, self.data[2])
            driver.F5()
            self.second = driver.get_table_text()
            self.screenshots = driver.screen_base64_shot()
            self.assertNotEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise
