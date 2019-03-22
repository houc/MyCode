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


class MarketingTransformationElement(OperationElement):
    """
    封装"MarketingTransformationElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================

    hover = (By.XPATH, "(//tr[starts-with(@class, 'ivu-table-row')])[1]")
    select = (By.XPATH, "(//div[@class='m-menu-handle']/div/div/div/i)[$]") # 1:复制，2:编辑，3:删除
    up = (By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[2]")

    def test_element(self, location):
        self.hovers(self.hover)
        self.is_click(self.str_conversion(self.select, location))

    def assert_url(self):
        return self.is_url_contain(url="marketing_mail_id")

    def ups(self):
        self.operation_element(self.up).send_keys('D:\\work_file\\auto_script\\UI\\img\\logo.png')