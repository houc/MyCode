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
class CompanyManage(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": '15882223197', "password": 'Bb123456', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    def test_open_company_info(self):
        """
        打开验证公司信息维护，验证账户管理是否存在

        1、使用超管账号，进入权限管理后台，切换至{公司管理}，打开{公司信息维护}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/notice/list};

        3、验证是否存在{账户管理}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'],
                                    driver=self.driver, name='方坤')
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[1], self.data[0])
            driver.get(self.url)
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[1])
                driver.screen_shot(self.screenshots_path)
                self.assertEqual(message, self.data[2])
                driver.get(driver.home_url)
                return self.test_open_company_info()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[3])
            driver.F5()
            self.first = driver.get_title(self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_close_company_info(self):
        """
        关闭验证公司信息维护，验证账户管理是否存在

        1、使用超管账号，进入权限管理后台，切换至{公司管理}，关闭{公司信息维护}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/notice/list};

        3、验证是否存在{账户管理}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'],
                                    driver=self.driver, name='方坤')
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[1], self.data[0])
            driver.get(self.url)
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[1])
                driver.screen_shot(self.screenshots_path)
                self.assertEqual(message, self.data[2])
                driver.get(driver.home_url)
                return self.test_close_company_info()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[3])
            driver.F5()
            self.first = driver.get_title(self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_close_user_manage(self):
        """
        关闭验证用户管理，验证用户和部门是否存在

        1、使用超管账号，进入权限管理后台，切换至{公司管理}，关闭{用户管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/notice/list};

        3、验证是否存在{用户和部门}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'],
                                    driver=self.driver, name='方坤')
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[1], self.data[0])
            driver.get(self.url)
            if 'true' == name_and_switch[1]:
                message = driver.message_box(self.data[1])
                driver.screen_shot(self.screenshots_path)
                self.assertEqual(message, self.data[2])
                driver.get(driver.home_url)
                return self.test_close_user_manage()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[3])
            driver.F5()
            self.first = driver.get_title(self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

    def test_open_user_manage(self):
        """
        开启验证用户管理，验证用户和部门是否存在

        1、使用超管账号，进入权限管理后台，切换至{公司管理}，开启{用户管理}权限，并提示{权限更新成功};

        2、使用设置的账号访问{/#/manage/notice/list};

        3、验证是否存在{用户和部门}
        """
        try:
            driver = JurisdictionElement(self.driver)
            driver.get_current_name(self.LOGIN_INFO['account'], self.LOGIN_INFO['password'],
                                    driver=self.driver, name='方坤')
            driver.get(self.url)
            name_and_switch = driver.execute_op(self.data[1], self.data[0])
            driver.get(self.url)
            if 'false' == name_and_switch[1]:
                message = driver.message_box(self.data[1])
                driver.screen_shot(self.screenshots_path)
                self.assertEqual(message, self.data[2])
                driver.get(driver.home_url)
                return self.test_open_user_manage()
            driver.get(driver.member_list_url)
            account = driver.get_set_member_account(name_and_switch[0])
            LoginPublic(self.driver, account, 'Li123456', module=None).login(False)
            driver.get(driver.url + self.data[3])
            driver.F5()
            self.first = driver.get_title(self.data[-1])
            driver.screen_shot(self.screenshots_path)
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())

