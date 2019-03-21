import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from SCRM.data_report.currency import DataReportElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestContactsReport(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    @unittest.skip('暂时跳过！')
    def test_switchCompany(self):
        """
        进入联系人报表选择公司验证公司按钮是否选择成功:

        1、通过url访问数据报表;

        2、点击公司;

        """
        try:
            driver = DataReportElement(self.driver)
            driver.get(self.url)
            driver.table_click(value=3)
            value = driver.table_switch(value=3, text="active")
            time.sleep(2)
            if value:
                driver.screen_shot(self.screenshots_path)
                self.first = "正确"  # 此项为必填，第一个断言值
            else:
                driver.screen_shot(self.screenshots_path)
                self.first = "不正确"  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_valueDefault(self):
        """
        进入联系人报表选择公司验证默认选中按钮:

        1、通过url访问数据报表;

        2、验证是否选中【自己】;

        """
        try:
            driver = DataReportElement(self.driver)
            driver.get(self.url)
            driver.F5()
            value = driver.table_switch(value=2, text="active")
            time.sleep(2)
            if value:
                driver.screen_shot(self.screenshots_path)
                self.first = "正确"  # 此项为必填，第一个断言值
            else:
                driver.screen_shot(self.screenshots_path)
                self.first = "不正确"  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_contactsIncrease(self):
        """
        进入联系人报表选择公司验证新增联系人分布，新增联系人后是否+1:

        1、通过url访问数据报表;

        2、进入新增联系人统计报告数值;

        3、新增联系人;

        4、在进入新增联系人统计报告是否+1
        """
        try:
            driver = DataReportElement(self.driver)
            driver.get(self.url)
            value = driver.graphical_data(location=10)
            content = time.strftime("%Y%m%d%H%M%S") + "@qq.com"
            driver.add_contacts(location=2, text="请输入邮箱", content=content, save=6)
            driver.F5()
            driver.get(self.url)
            value_1 = driver.graphical_data(location=10)
            time.sleep(2)
            if not value == value_1:
                driver.screen_shot(self.screenshots_path)
                self.first = "正确"  # 此项为必填，第一个断言值
            else:
                driver.screen_shot(self.screenshots_path)
                self.first = "不正确"  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_contactsIncreaseStock(self):
        """
        进入联系人报表选择公司验证存量联系人分布，新增联系人后是否+1:

        1、通过url访问数据报表;

        2、进入存量联系人统计报告数值;

        3、新增联系人;

        4、在进入存量联系人统计报告是否+1
        """
        try:
            driver = DataReportElement(self.driver)
            driver.get(self.url)
            value = driver.graphical_data(location=9)
            content = time.strftime("%Y%m%d%H%M%S") + "@qq.com"
            driver.add_contacts(location=2, text="请输入邮箱", content=content, save=6)
            driver.F5()
            driver.get(self.url)
            value_1 = driver.graphical_data(location=9)
            time.sleep(2)
            if not value == value_1:
                driver.screen_shot(self.screenshots_path)
                self.first = "正确"  # 此项为必填，第一个断言值
            else:
                driver.screen_shot(self.screenshots_path)
                self.first = "不正确"  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_contactsDownload(self):
        """
        进入联系人报表下载报告是否成功:

        1、通过url访问数据报表;

        2、点击下载报告;

        3、验证是否成功下载;

        """
        try:
            driver = DataReportElement(self.driver)
            driver.get(self.url)
            driver.F5()
            result = driver.download_report(location=1, message_location=1)
            driver.screen_shot(self.screenshots_path)
            self.first = result  # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

    def test_selectTrimester(self):
        """
        进入联系人报表时间选择进3个月是否成功:

        1、通过url访问数据报表;

        2、点击近三个月;

        3、验证是否选择成功;

        """
        try:
            driver = DataReportElement(self.driver)
            driver.get(self.url)
            result = driver.time_table(location=2)
            driver.screen_shot(self.screenshots_path)
            self.first = result # 此项为必填，第一个断言值
        except Exception:
            self.error = str(traceback.format_exc())

if __name__ == '__main__':
    unittest.main()