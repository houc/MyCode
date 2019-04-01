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


class TechnologyElement(OperationElement):
    """
    封装"TechnologyElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    technology_table = (By.XPATH, "(//div[contains(@style, 'padding-left')])[$]")
    info = (By.XPATH, "(//li[@class='youimg'])[$]")

    def technology_table_click(self, location):
        """
        technology title的点击以及切换
        :param location: 1:Download, 2:Equipment, 3:Technology
        :return: ...
        """
        self.is_click(self.str_conversion(self.technology_table, location))

    def img_info(self, location):
        """
        点击图片详情
        :param location: 第几张图片
        :return: ...
        """
        self.is_click(self.str_conversion(self.info, location))
