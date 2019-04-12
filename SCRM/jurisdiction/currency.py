import requests
import time

from model.Yaml import MyProject, MyConfig
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


class JurisdictionElement(OperationElement):
    """
    封装"JurisdictionElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================
    login_url = MyConfig('url').base_url + ''
    member_list_url = MyConfig('url').base_url + '/#/manage/staff/staff-entry/staff-table'
    
    # ================================================元素==========================================
    dept = (By.XPATH, "(//div[starts-with(@class, 'in-item')])[$]") # 部门选择
    member = (By.XPATH, "(//div[starts-with(@class, 'in_member')])[$]") # 人员选择
    role = (By.XPATH, "//td[contains(text(), '$')]/../td[2]/span") # 权限选择
    is_role = (By.XPATH, "//td[contains(text(), '$')]/../td[2]/span/input") # 判断对应的权限是否开启或者是关闭
    message = (By.XPATH, "(//div[@class='ivu-message'])[1]/div/div/div/div/span")  # 消息提示框
    get_user_name = (By.XPATH, "(//div[@mode='in-out'])[2]")  # 当前设置人员的名字
    member_search = (By.XPATH, "//input[starts-with(@class, 'ivu-input')]") # 人员搜索框的列表


    def _dept_and_member(self, location=2):
        """
        部门和人员选择
        :param location: 位置
        :return: 返回设置人员的名字
        """
        self.is_click(self.str_conversion(self.dept, location))
        time.sleep(1)
        self.is_click(self.str_conversion(self.member, location))
        time.sleep(1)
        return self.is_text(self.get_user_name)

    def _role_table(self, role_name):
        """
        权限的名称点击对应的开关
        :param role_name: 导入
        :return: ...
        """
        self.is_click(self.str_conversion(self.role, role_name))

    def _is_role_switch_false(self, role_name):
        """
        判断权限是否关闭
        :param role_name: 权限名称
        :return: 返回对应的bool值
        """
        return self.is_attribute_value(self.str_conversion(self.is_role, role_name), 'false')

    def execute_op(self, role_name):
        """
        获取设置权限人员的账号
        :param role_name: 权限的名字
        :return: 设置人员的姓名，bool值
        """
        return self._dept_and_member(), self._is_role_switch_false(role_name)

    def message_box(self, role_name):
        """
        获取消息弹窗
        :param role_name: 权限名称
        :return: 返回对应的弹窗名称
        """
        self._role_table(role_name)
        return self.is_text(self.message)
