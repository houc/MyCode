import requests
import time

from model.Yaml import MyProject, MyConfig
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from SCRM.common import LoginPublic

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
    home_url = MyConfig('url').base_url + '/#/home'
    member_list_url = MyConfig('url').base_url + '/#/manage/staff/staff-entry/staff-table'
    customer_url = MyConfig('url').base_url + '/#/sale/customer'
    contact_url = MyConfig('url').base_url + '/#/sale/contact'
    field_url = MyConfig('url').base_url + '/#/manage/salesManagement/filed?state=contact'
    url = MyConfig('url').base_url
    
    # ================================================元素==========================================
    dept = (By.XPATH, "(//div[starts-with(@class, 'in-item')])[$]") # 部门选择
    member = (By.XPATH, "(//div[starts-with(@class, 'in_member')])[$]") # 人员选择
    role = (By.XPATH, "//td[contains(text(), '$')]/../td[2]/span") # 权限选择
    is_role = (By.XPATH, "//td[contains(text(), '$')]/../td[2]/span/input") # 判断对应的权限是否开启或者是关闭
    message = (By.XPATH, "(//div[@class='ivu-message'])[1]/div/div/div/div/span")  # 消息提示框
    get_user_name = (By.XPATH, "(//div[@mode='in-out'])[2]")  # 当前设置人员的名字
    member_search = (By.XPATH, "//input[starts-with(@class, 'ivu-input')]") # 人员搜索框的列表
    set_account = (By.XPATH, "(//div[@class='ivu-table-cell'])[$]") # 搜索人员的列表对应值
    customer_button = (By.XPATH, "//div[contains(text(), '$')]") # 验证模块是否存在
    get_login_name = (By.XPATH, "//span[@class='head_a']/span") # 当前登录人员的名字
    customer_box = (By.XPATH, "//tbody[@class='ivu-table-tbody']/tr[$]/td/div/label") # 客户选择框
    jurisdiction = (By.XPATH, "(//span[text()='$'])[1]/..") # 小的权限框
    title_table = (By.XPATH, "//span[contains(text(), '$')]") # 左侧权限是否存在
    left_table = (By.XPATH, "//li[contains(text(), '$')]") # 左边靠中间是否存在
    title_switch = (By.XPATH, "//div[text()='$ ']") # 权限的table切换，如切换到公司管理
    notice_status = (By.XPATH, "//td[text()='$']/../td[2]/span/input") # 公告状态


    def _dept_and_member(self, location=2):
        """
        部门和人员选择
        :param location: 位置
        :return: 返回设置人员的名字
        """
        self.is_click(self.str_conversion(self.dept, location))
        self.is_click(self.str_conversion(self.member, location))
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
        return self.get_attribute_value(self.str_conversion(self.is_role, role_name))

    def execute_op(self, role_name, table_switch='', dept_location=2, member_location=1):
        """
        获取设置权限人员的账号,并执行后台方法
        :param role_name: 权限的名字
        :param table_switch: 是否table切换
        :return: 设置人员的姓名，bool值
        """
        if table_switch:
            self.is_click(self.str_conversion(self.dept, dept_location))
            self.is_click(self.str_conversion(self.member, member_location))
            name = self.is_text(self.get_user_name)
            self.is_click(self.str_conversion(self.title_switch, table_switch))
            return name, self._is_role_switch_false(role_name)
        else:
            return self._dept_and_member(), self._is_role_switch_false(role_name)

    def message_box(self, role_name):
        """
        获取消息弹窗
        :param role_name: 权限名称
        :return: 返回对应的弹窗名称
        """
        self._role_table(role_name)
        return self.is_text(self.message)

    def get_set_member_account(self, name, location=14):
        """
        获取设置的员工账号
        :param name 员工的姓名
        :return: ...
        """
        self.is_send(self.member_search, name)
        self.operation_element(self.member_search).send_keys(Keys.ENTER)
        return self.is_text(self.str_conversion(self.set_account, location))

    def module_switch(self, module):
        """
        验证权限模块是否存在
        :param module: 导入/导出
        :return: 返回对应值是否存在
        """
        return self.is_element(self.str_conversion(self.customer_button, module))

    def get_current_name(self, account, password, name='超超', driver=None):
        """
        获取当前登录人姓名
        :param name: 姓名
        :return: 返回当前登录人姓名
        """
        get_name = self.is_text(self.get_login_name, name)
        if not name == get_name:
            LoginPublic(driver, account, password, module=None).login(False)

    def get_customer_button(self, role_name, location=1):
        """
        获取客户小权限的开启情况
        :param role_name: 权限名称
        :param location: 默认的位置
        :return: 返回对应的获取值
        """
        self.is_click(self.str_conversion(self.customer_box, location))
        return self.is_element(self.str_conversion(self.jurisdiction, role_name))

    def get_title(self, module):
        """
        获取左侧权限开启情况
        :param module: 权限名称
        :return: 返回对应权限名称
        """
        return self.is_element(self.str_conversion(self.title_table, module))

    def is_module(self, role_name):
        """
        点击模块
        :param role_name: 执行的模块
        :return:
        """
        self._is_role_switch_false(role_name)

    def get_left_tab(self, module):
        """
        获取左边元素是否存在
        :param module: 权限名称
        :return: 返回对应是否存在
        """
        return self.is_element(self.str_conversion(self.left_table, module))

    def get_notice_status(self, role_name, dept_location=2, member_location=1, table_switch='', notice='公告'):
        """
        公告名称
        :param role_name: 公告
        :return:
        """
        self.is_click(self.str_conversion(self.dept, dept_location))
        self.is_click(self.str_conversion(self.member, member_location))
        name = self.is_text(self.get_user_name)
        self.is_click(self.str_conversion(self.title_switch, table_switch))
        status = self.get_attribute_value(self.str_conversion(self.notice_status, notice))
        if 'false' == status:
            self.message_box(notice)
        return name, self.get_attribute_value(self.str_conversion(self.is_role, role_name))
