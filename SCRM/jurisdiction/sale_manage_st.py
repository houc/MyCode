import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from SCRM.jurisdiction.currency import JurisdictionElement
from SCRM.common import LoginPublic

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class SaleManage(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15928564313', "password": 'Aa123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    def test_close_import(self):
        """
        关闭导入权限，验证导入按钮是否存在

        1、使用超管账号，进入权限管理后台，关闭{导入}权限，并提示{权限更新成功};

        2、使用设置的账号进行验证{导入客户/联系人}是否存在;
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_import()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.customer_url)
            driver.F5()
            first = driver.module_switch(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_open_import(self):
        """
        开启导入权限，验证导入按钮是否存在

        1、使用超管账号，进入权限管理后台，开启{导入}权限，并提示{权限更新成功};

        2、使用设置的账号进行验证{导入客户/联系人}是否存在;
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_import()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.customer_url)
            driver.F5()
            first = driver.module_switch(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    # @unittest.skip('')
    def test_close_export(self):
        """
        关闭导出权限，验证导出按钮是否存在

        1、使用超管账号，进入权限管理后台，关闭{导出}权限，并提示{权限更新成功};

        2、使用设置的账号进行验证{导出联系人}是否存在;
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_export()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.customer_url)
            driver.F5()
            first = driver.get_customer_button(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_open_export(self):
        """
        开启导出权限，验证导出按钮是否存在

        1、使用超管账号，进入权限管理后台，开启{导出}权限，并提示{权限更新成功};

        2、使用设置的账号进行验证{导出联系人}是否存在;
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_export()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.customer_url)
            driver.F5()
            first = driver.get_customer_button(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_open_distribution(self):
        """
        开启分配权限，验证分配按钮是否存在

        1、使用超管账号，进入权限管理后台，开启{分配}权限，并提示{权限更新成功};

        2、使用设置的账号进行验证{分配}是否存在;
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_distribution()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.customer_url)
            driver.F5()
            first = driver.get_customer_button(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_close_distribution(self):
        """
        关闭分配权限，验证分配按钮是否存在

        1、使用超管账号，进入权限管理后台，关闭{分配}权限，并提示{权限更新成功};

        2、使用设置的账号进行验证{分配}是否存在;
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_distribution()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.customer_url)
            driver.F5()
            first = driver.get_customer_button(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    # @unittest.skip('')
    def test_open_field(self):
        """
        开启设置属性字段分配权限，验证设置属性字段是否存在

        1、使用超管账号，进入权限管理后台，关闭{设置属性字段}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/filed?state=contact};

        3、跳转到{/#/home}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_field()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_close_field(self):
        """
        开启设置属性字段分配权限，验证设置属性字段是否存在

        1、使用超管账号，进入权限管理后台，关闭{设置属性字段}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/filed?state=contact};

        3、跳转到{/#/home}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_field()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.field_url)
            driver.F5()
            first = driver.is_url_contain(self.data[-1])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_close_tag(self):
        """
        关闭标签管理权限，验证标签管理是否存在

        1、使用超管账号，进入权限管理后台，关闭{标签管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/tag?state=contact};

        3、跳转到{/#/home}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_tag()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[-1])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    # @unittest.skip('')
    def test_open_tag(self):
        """
        开启标签管理权限，验证标签管理是否存在

        1、使用超管账号，进入权限管理后台，开启{标签管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/tag?state=contact};

        3、跳转到{/#/home}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0]) # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_tag()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_open_public(self):
        """
        开启公海管理权限，验证公海管理是否存在

        1、使用超管账号，进入权限管理后台，开启{公海管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/globalClient/rule};

        3、验证{/#/home}是否存在
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0])  # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_public()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    # @unittest.skip('')
    def test_close_public(self):
        """
        关闭公海管理权限，验证公海管理是否存在

        1、使用超管账号，进入权限管理后台，关闭{公海管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/globalClient/rule};

        3、验证{/#/home}是否存在
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0])  # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_public()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[3])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())


    def test_open_private(self):
        """
        开启私海管理权限，验证私海管理是否存在

        1、使用超管账号，进入权限管理后台，开启{私海管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/selfNum};

        3、验证{/#/home}是否存在
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0])  # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_open_private()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[2])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    # @unittest.skip('')
    def test_close_private(self):
        """
        关闭私海管理权限，验证私海管理是否存在

        1、使用超管账号，进入权限管理后台，关闭{私海管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/salesManagement/selfNum};

        3、验证{/#/home}是否存在
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'], driver=self.driver)
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[0])  # 0设置员工的姓名，1获取当前的权限是否是开启或者是关闭状态
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[0])
                self.assertEqual(message, self.data[1])
                driver.screen_shot(self.screenshots_path)
                driver.get(driver.home_url)
                return self.test_close_private()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[2])
            driver.F5()
            first = driver.is_url_contain(self.data[3])
            if not first:
                self.first = False
            else:
                self.first = True
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
