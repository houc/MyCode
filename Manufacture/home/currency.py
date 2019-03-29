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


class HomeElement(OperationElement):
    """
    封装"HomeElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    table = (By.XPATH, "(//a[starts-with(@class, 'Fourm')])[$]")
    new_table = (By.XPATH, "(//div[@class='bodr'])[$]/a[1]")

    def table_click(self, location):
        """
        table测试的位置
        :param location: 1:About Us, 2:Products Center, 3:Technological Strength, 4:Contact Us
        :return: ...
        """

        self.is_click(self.str_conversion(self.table, location))

    def new_table_click(self, location):
        """
        newCenter断言值l
        :param location: 1:news一，2:news二，3:launching
        :return: ..
        """
        self.is_click(self.str_conversion(self.new_table, location))

    def news_assert(self, url):
        """
        news断言值
        :param url: /news/71.html
        :return: 返回对应的url是否正确
        """
        return self.is_url_contain(url)