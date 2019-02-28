import requests
import random
import string
import time
import datetime

from model.SeleniumElement import ElementLocation
from model.GetToken import BrowserToken
from model.MyConfig import ConfigParameter
from model.Yaml import MyYaml


class LoginTestModules(object):
    # ======================================元素==================================================================== #

    account_element_1 = "//*[text()='手机号/邮箱']/../div[1]/input!!click"
    account_element_2 = "//*[text()='手机号/邮箱']/../div[1]/input!!send"
    password_element_1 = "//*[text()='密码']/../div[1]/input!!click"
    password_element_2 = "//*[text()='密码']/../div[1]/input!!send"
    login_element = "//*[text()='登录']/..!!click"
    # company_element = '请选择要登录的公司*/../../div[2]/div/div/div/ul/li[1]!!click'
    assert_success = "//*[text()='哒哒']/.!!text"
    is_open = "//*[text()='账号密码登录']!!text"

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url + '/platform/#/account/login'

    def success_login(self, account, password):
        """登录成功"""
        element = ElementLocation(self.driver)
        element.get(self.url)
        time.sleep(3)
        element.F5()
        element.XPATH(self.account_element_1)
        element.XPATH(self.account_element_2, account)
        element.XPATH(self.password_element_1)
        element.XPATH(self.password_element_2, password)
        element.XPATH(self.login_element)
        time.sleep(1)
        assert element.XPATH(self.assert_success) == "哒哒"
        BrowserToken(self.driver).get_token()

    def opens_if(self):
        """网址是否打开"""
        element = ElementLocation(self.driver)
        element.get(self.url)
        time.sleep(3)
        element.F5()
        assert element.XPATH(self.is_open) == "账号密码登录"


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