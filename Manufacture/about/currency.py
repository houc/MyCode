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


class AboutElement(OperationElement):
    """
    封装"AboutElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    about_us_table = (By.XPATH, "(//div[contains(@style, 'padding-left')])[$]")
    next_page = (By.XPATH, "//div[starts-with(@class, 'next')]")
    img = (By.XPATH, "//div[contains(@class, 'p_AtlasList')]/div[1]/div[$]")

    def about_table_click(self, location):
        """
        aboutUs title的点击以及切换
        :param location: 1:Profile，2:Speech，3:Organization，4:Philosophy，5:Honor，6:Staff Style
        :return: ...
        """
        self.is_click(self.str_conversion(self.about_us_table, location))

    def about_next_click_page(self):
        """
        点击下一页操作
        :return:
        """
        self.is_click(self.next_page)

    def img_click(self, location):
        """
        带图片点击元素
        :param location: 图片第几张
        :return: ...
        """
        self.is_click(self.str_conversion(self.img, location))