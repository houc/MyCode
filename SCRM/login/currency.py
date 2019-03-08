import requests
import time

from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import ElementLocation
from selenium.webdriver.common.by import By

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


class LoginElement(ElementLocation):
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
    is_open = (By.XPATH, "//div[text()='账号密码登录 ']/.")

    def error_account(self, value):
        """错误的账号登录"""
        self.find_element(self.account_element).send_keys(value)
