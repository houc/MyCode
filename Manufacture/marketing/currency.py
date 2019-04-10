import requests
import time

from model.Yaml import MyProject
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
    read = MyProject(UP_FILE_NAME, keys).module_data
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
    return ConfigParameter().read_ini()


class MarketingElement(OperationElement):
    """
    封装"MarketingElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    market = (By.XPATH, '(//a[@href="/nav/13.html"]/span[1])')
    concept = (By.XPATH, '(//div[contains(@title, "Concept")])')
    network = (By.XPATH, '(//div[contains(@title, "Network")])')
    marketing_knowledge = (By.XPATH, '(//div[contains(@title, "Marketing knowledge")])')
    market_about = (By.XPATH,'//a[@href="/nav/51.html"]/div/div')
    market_about_profile = (By.XPATH,'//a[@href="/nav/52.html"]/div/div')

    def market_click(self):
        """
        market测试的位置
        :param : marketing
        :return: ...
        """
        self.is_click(self.market)

    def concept_click(self):
        """
        concept测试位置
        :return:
        """
        self.is_click(self.concept)

    def network_click(self):
        """
        concept测试位置
        :return:
        """
        self.is_click(self.network)

    def marketing_knowledge_click(self):
        """
        concept测试位置
        :return:
        """
        self.is_click(self.marketing_knowledge)
