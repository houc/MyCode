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


class LoginElement(OperationElement):
    """
    封装"LoginElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    
    # ================================================元素==========================================
    mail = (By.XPATH, "(//tr[@class='ivu-table-row'])[$]")

    def assert_mail(self, location=1):
        """
        获取邮件是否获取成功
        :param location: 1
        :return: bool
        """
        return self.is_element(self.parametrization(self.mail, location))