import requests
import time

from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def read_currency(keys: str, line: int):
    """
    读取currency.ya中的数据
    Usage: 
        url = MyYaml("SCRM").base_url + read_currency("get_customer", 0)
        data = read_currency("get_customer", 1)
    """
    data = []
    read = MyYaml(UP_FILE_NAME).ModulePublic[keys]
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]

def token():
    """
    获取token值
    Usage:
        r = requests.post(url, headers=token(), data=data, stream=True)
    """
    token = ConfigParameter().read_ini()
    return token


class LoginElement(OperationElement):
    """
    封装"LoginElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """

    # ================================================元素==========================================

    account_element = (By.XPATH, "//*[contains(text(),'手机号/邮箱')]/../input")
    password_element = (By.XPATH, "//*[contains(text(),'密码')]/../input")
    login_element = (By.XPATH, "//button[contains(text(),'登录')]")
    company_element = (By.XPATH, "//li[contains(text(),'$')]")
    isExist_company = (By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")
    assert_success = (By.XPATH, "(//span[text()='$'])[1]/.")
    assert_error_message = (By.XPATH, "//div[contains(text(), '$')]/.")
    is_open = (By.XPATH, "//div[text()='账号密码登录 ']/.")

    def login_param(self, account, password, company=None):
        """登录信息"""
        self.operation_element(self.account_element).send_keys(Keys.CONTROL, "a")
        self.operation_element(self.account_element).send_keys(Keys.ENTER)
        self.operation_element(self.account_element).send_keys(account)
        self.operation_element(self.password_element).send_keys(Keys.CONTROL, "a")
        self.operation_element(self.password_element).send_keys(Keys.ENTER)
        self.operation_element(self.password_element).send_keys(password)
        time.sleep(1)
        self.operation_element(self.login_element).click()
        exist = self.is_element(self.isExist_company)
        if exist:
            if company is None:
                raise TypeError("该账号有多个公司company需要传参数，不能为空")
            self.operation_element(self.str_conversion(self.company_element, company)).click()

    def assert_login(self, value):
        """
        断言信息参数
        :param value: 断言的参数信息，如：小明
        :return: 返回对应参数
        """
        return self.operation_element(self.str_conversion(self.assert_error_message, value)).text

    def success_assert(self, value):
        """
        登录成功后的断言信息
        :param value: 断言参数，如：小明
        :return:
        """
        return self.operation_element(self.str_conversion(self.assert_success, value)).text
