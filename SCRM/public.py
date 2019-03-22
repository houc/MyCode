import requests
import random
import string
import time
import datetime

from model.SeleniumElement import OperationElement
from model.GetToken import BrowserToken
from model.MyConfig import ConfigParameter
from model.Yaml import MyYaml
from selenium.webdriver.common.by import By


class LoginTestModules(OperationElement):
    # ======================================URL====================================================================

    Login_URL = MyYaml("SCRM").base_url + "/#/account/login"

    # ======================================元素==================================================================== #

    account_element = (By.XPATH, "//*[contains(text(), '手机号/邮箱')]/../input")
    password_element = (By.XPATH, "//*[contains(text(), '密码')]/../input")
    login_element = (By.XPATH, "//button[contains(text(), '登录')]")
    company_element = (By.XPATH, "//li[contains(text(), '$')]")
    isExist_company = (By.XPATH, "//*[contains(text(), '请选择要登录的公司')]")
    assert_success = (By.XPATH, "(//span[text()='$'])[1]/.")
    is_open = (By.XPATH, "//div[text()='账号密码登录 ']/.")

    def __init__(self, driver):
        super(LoginTestModules, self).__init__(driver)

    def success_login(self, account, password, company=None):
        """登录成功"""
        self.get(self.Login_URL)
        self.operation_element(self.account_element).send_keys(account)
        self.operation_element(self.password_element).send_keys(password)
        self.operation_element(self.login_element).click()
        exist = self.operation_element(self.isExist_company)
        if exist:
            if company is None:
                raise TypeError("该账号存在多家公司，请传入company是属于哪家公司进行登录！")
            self.operation_element(self.str_conversion(self.company_element, company)).click()
        assert self.operation_element(self.str_conversion(self.assert_success, "超人")).text == "超人"
        # time.sleep(3)
        BrowserToken(self.driver).get_token()

    def opens_if(self):
        """网址是否打开"""
        self.get(self.Login_URL)
        assert self.operation_element(self.is_open).text == "账号密码登录"


class Interface(object):
    """该类主要公共方法的接口辅助"""
    def __init__(self):
        self.token = ConfigParameter().read_ini()
        self.public = MyYaml().AllPublicData
        self.url = MyYaml('Interface').base_url
        self.requests = requests.session()

    def add_staff(self):
        """使用接口添加员工"""
        url =  self.url + self.read_public('add_staff', 0)
        number = ''.join(str(i) for i in random.sample(range(0, 9), 9))
        data = self.read_public('add_staff', 1)
        letter = ''.join(random.sample(string.ascii_uppercase, 4)) + number[: -4]
        data["form_data"] = data["form_data"] % ( '31测试' + letter, '13' + number, number + '@qq.com')
        r = self.requests.post(url, headers=self.token, data=data, stream=True)
        print(r.json())
        print(r.elapsed.total_seconds())

    def read_public(self, key, line):
        """读取public.ya文件"""
        data = []
        for i in self.public[key]:
            data.append(i["url"])
            data.append(i["bar"])
        return data[line]

    def get_staff(self, status=2):
        """
        在在职员工列表中获取员工的id
        :param status: 1在职员工列表；2冻结员工里面；0离职员工列表
        """

        member_ids = []
        url = self.url + self.read_public('get_staff', 0)
        data = self.read_public('get_staff', 1)
        data["status"] = status
        r = self.requests.post(url, headers=self.token, data=data, stream=True)
        if r.json().get("code") == 0:
            member_list = r.json().get("data")
            for member in member_list:
                member_ids.append(member.get("member_id"))
            return member_ids
        else:
            print(r.json())

    def frozen_staff(self):
        """冻结员工"""
        member_ids = self.get_staff()
        url = self.url + self.read_public('frozen_staff', 0)
        data = self.read_public('frozen_staff', 1)
        if member_ids:
            for a in member_ids:
                data["member_ids"] = a
                r = self.requests.post(url, headers=self.token, data=data, stream=True)
                print(r.json())
                print(r.elapsed.total_seconds())
        else:
            print("对应列表中无员工，请检查状态参数")

    def quit_staff(self):
        """设为离职员工"""
        member_ids = self.get_staff()
        url = self.url + self.read_public('quit_staff', 0)
        data = self.read_public('quit_staff', 1)
        if member_ids:
            for a in member_ids:
                data["member_ids"] = a
                data["leave_date"] = (datetime.datetime.now() - datetime.timedelta(days=1)).\
                    strftime('%Y-%m-%d %H:%M:%S')
                r = self.requests.post(url, headers=self.token, data=data, stream=True)
                print(r.json())
                print(r.elapsed.total_seconds())
        else:
            print("对应列表中无员工，请检查状态参数")

    def login_staff(self, account, password='Aa123456'):
        """员工登录"""
        url = self.url + self.read_public('login_staff', 0)
        data = self.read_public('login_staff', 1)
        data["account"] = account
        data["password"] = password
        r = self.requests.post(url, data=data, stream=True)
        print(r.json())

    def add_fields(self):
        """添加员工属性"""
        url = self.url + self.read_public('add_fields', 0)
        data = self.read_public('add_fields', 1)
        data["title"] = time.strftime('%S')

        r = self.requests.post(url, headers=self.token, data=data, stream=True)
        print(r.json())

    def add_config(self, value=1):
        """客户画像管理"""
        url = self.url + self.read_public('add_config', 0)
        data = self.read_public('add_config', 1)
        data["type"] = value
        data["title"] = time.strftime('%H%M%S')
        r = self.requests.post(url, headers=self.token, data=data, stream=True)
        print(r.json())

    def add_tag(self):
        """添加客户标签"""
        number = ''.join(str(i) for i in random.sample(range(0, 9), 9))
        letter = ''.join(random.sample(string.ascii_uppercase, 4)) + number[: -4]
        url = self.url + self.read_public('add_tag', 0)
        data = self.read_public('add_tag', 1)
        data["tag_name"] = (letter + number)[:10]
        r = self.requests.post(url, headers=self.token, data=data, stream=True)
        print(r.json())


if __name__ == '__main__':
    # Interface().login_staff('15926656565')
    # for i in range(9):
    #     Interface().add_config()
    for i in range(40):
        Interface().add_tag()
    # Interface().quit_staff()