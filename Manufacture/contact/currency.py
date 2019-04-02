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


class ContactElement(OperationElement):
    """
    封装"ContactElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    contact = (By.XPATH, "(.//div[@id='menu2']/ul/li[7])")
    ContactUs = (By.XPATH, "(//div[@title='Contact Us'])")
    Message = (By.XPATH, "(//div[@title='Message'])")


    def contact_click(self):
        """
        contact断言值
        :param url: /nev/24.html
        :return: 返回对应的url是否正确
        """
        return self.is_click(self.contact)

    def contacts_click(self):
        """
        contactUs断言值
        :param url: /intro/13.html
        :return: 返回对应的url是否正确
        """
        return self.is_click(self.ContactUs)

    def message_click(self):
        """
        Message断言值
        :param url: /messages.html
        :return: 返回对应的url是否正确
        """
        return self.is_click(self.Message)