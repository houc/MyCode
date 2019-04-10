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
    table_num = (By.XPATH, "(//div[@class='ws-stat-num'])[$]/div[1]") # 工作成效
    quick = (By.XPATH, "//span[text()='$']/..") # 快捷键操作
    addressee = (By.XPATH, "//div[@id='addText']/input") # 收件人输入框
    theme = (By.XPATH, "//div[@class='topic']/input") # 邮件发送主题
    send = (By.XPATH, "//div[@class='top-operation']/button[1]") # 邮件发送按钮

    def work_num(self, location):
        """
        工作成效
        :param location: 1；发送普通邮件，2；发送营销邮件，3；收到邮件，4；新增联系人，5；新增客户
        :return: 返回对应数值
        """
        return self.is_text(self.str_conversion(self.table_num, location))

    def quick_button(self, text):
        """
        快捷键操作
        :param text: 新建邮件
        :return: ...
        """
        self.is_click(self.str_conversion(self.quick, text))

    def add_mail(self, addressee, theme):
        """
        发送邮件
        :param addressee: 收件人
        :param theme: 主题
        :return: ...
        """
        self.is_send(self.addressee, addressee)
        self.is_send(self.theme, theme)
        self.is_click(self.send)
