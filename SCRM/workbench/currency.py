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
        url = MyProject("SCRM").base_url + read_currency("get_customer", 0)
        data = read_currency("get_customer", 1)
    """
    data = []
    read = MyProject(UP_FILE_NAME, keys).module_data
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]


def token(module):
    """
    获取token值,module:获取的值
    Usage:
        r = requests.post(url, headers=token(module), data=data, stream=True)
    """
    return ConfigParameter().read_ini(node=module)


class WorkbenchElement(OperationElement):
    """
    封装"WorkbenchElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    # ================================================元素==========================================
    quick_table = (By.XPATH, "(//div[@class='ws-quick-item'])[$]/span")
    result_table = (By.XPATH, "(//div[@class='ws-stat-num'])[$]/div[2]")

    def opera_quick(self, action):
        transfer1 = self.parametrization(self.quick_table, action)
        return self.get_text(transfer1)

    def result_opera(self, action):
        transfer1 = self.parametrization(self.result_table, action)
        return self.get_text(transfer1)
