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


class NewsElement(OperationElement):
    """
    封装"NewsElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    news_us_table = (By.XPATH, "(//div[contains(@style, 'padding-left')])[$]")
    news_info = (By.XPATH, "//ul[@class='news_two_ul']/li[$]")
    next_page = (By.XPATH, "//div[starts-with(@class, 'next')]")
    company_info = (By.XPATH, "(//li[@class='youimg'])[$]")

    def news_table_click(self, location):
        """
        news title的点击以及切换
        :param location: 1:Company News，2:Industry Dynamics，3:Notice，4:Knowledge，5:Public Welfare
        :param location: Company News 中调用使用中:1:Download, 2:Equipment, 3:Technology
        :return: ...
        """
        self.is_click(self.str_conversion(self.news_us_table, location))

    def news_info_click(self, location):
        """
        点击NewsCenter中数据进入详情
        :param location: 第几条数据
        :return: ...
        """
        self.is_click(self.str_conversion(self.news_info, location))

    def next_page_click(self):
        """
        点击下一页
        :return: ...
        """
        self.is_click(self.next_page)

    def company_img_info(self, location):
        """
        点击公司类型的图片进入对应的图片详情
        :param location: 第几张图片位置
        :return: ...
        """
        self.is_click(self.str_conversion(self.company_info, location))