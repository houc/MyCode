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
    input_button = (By.XPATH, "(//div[contains(text(), '输入')])[$]/following::input[1]") # 输入元素
    save_button = (By.XPATH, "(//span[contains(text(), '保存')])[$]/..") # 保存位置
    message = (By.XPATH, "(//div[@class='ivu-message'])[1]/div/div/div/div/span")  # 消息提示框
    country_select = (By.XPATH, "//div[contains(text(), '请选择国家')]/../div[2]") # 选择国家下拉框
    china = (By.XPATH, "//li[text()='$']")
    mail_text = (By.XPATH, "(//td[contains(@class, 'in-hd')])[$]") # 邮件位置汉字
    close_top_box = (By.XPATH, "(//span[contains(@class, 'ics-cuo')])[$]") # 关闭弹窗
    cancel = (By.XPATH, "(//button[starts-with(@class, 'g-btn-cancel')])[$]") # 取消
    process_element = (By.XPATH, "//div[text()='$']/../..") # 选择邮件类型
    confirm = (By.XPATH, "(//span[contains(text(), '确定')])[$]/..") # 确定的按钮
    process_week = (By.XPATH, "//span[text()='$']/../div[2]")  # 邮件流程周期
    mark_star = (By.XPATH, "(//div[@class='ivu-tooltip'])[4]/div/i") # 星标邮件
    get_user_name = (By.XPATH, "(//div[@class='ivu-dropdown'])[1]/div/span/span") # 当前登录人的元素
    select_member = (By.XPATH, "//span[text()='选择人员']/../div/div/input") # 选择人员输入框
    table = (By.XPATH, "(//div[contains(@class, 'ivu-tabs-tab')])[$]")  # 1:我的邮件， 2:联系人动态， 3:今日任务
    select_confirm = (By.XPATH, "//li[@class='search-list']/label") # 负责人的按钮


    def week_type(self, week='请选择日期相关属性', *, type):
        """
        流程周期类型选择
        :param week: 属性
        :param type: 类型
        :return: ...
        """
        self.is_click(self.str_conversion(self.process_week, week))
        self.is_click(self.str_conversion(self.china, type))

    def cancel_button(self, location):
        """
        取消按钮
        :param location: 位置
        :return: ...
        """
        self.is_click(self.str_conversion(self.cancel, location))

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

    def send_button(self):
        """
        发送按钮
        :return:
        """
        self.is_click(self.send)

    def add_contacts(self, input_location, mail):
        """
        增加联系人
        :param input_location: 具体输入框的位置
        :param mail: 邮件地址
        :return: ...
        """
        self.is_send(self.str_conversion(self.input_button, input_location), mail)

    def save(self, location, wait=20):
        """
        保存按钮的具体位置
        :param location:
        :return:
        """
        self.is_click(self.str_conversion(self.save_button, location), wait)

    def message_top_box(self):
        """
        消息弹窗
        :param text: 具体提示内容
        :return: 获取到的内容
        """
        return self.is_text(self.message)

    def add_customer(self, china, customer, location):
        self.is_click(self.country_select)
        self.is_click(self.str_conversion(self.china, china))
        self.is_send(self.str_conversion(self.input_button, location), customer)

    def text_mail(self, location):
        """
        邮件文字汉字
        :param location: 具体文字
        :return: 返回获取的文字
        """
        return self.is_text(self.str_conversion(self.mail_text, location))

    def close_box(self, location):
        """
        关闭弹窗
        :param location: 位置
        :return: ...
        """
        self.is_click(self.str_conversion(self.close_top_box, location))

    def marketing_type(self, text):
        """
        选择营销邮件流程
        :param location: 确定的位置
        :param text: 类型的文字
        :return: ...
        """
        self.is_click(self.str_conversion(self.process_element, text))

    def process_click(self, location=3):
        """流程的点击"""
        self.is_click(self.str_conversion(self.confirm, location))

    def mark_star_mail(self):
        """标记为星标邮件"""
        if self.is_attribute_class(self.mark_star, 'icon-ic_star_border_black'):
            self.is_click(self.mark_star)
        else:
            self.is_click(self.mark_star)
            time.sleep(5)
            self.mark_star_mail()

    def add_task(self, theme, member='负责人'):
        """"""
        name = self.is_text(self.get_user_name)
        self.is_send(self.str_conversion(self.input_button, 1), theme)
        self.is_click(self.str_conversion(self.quick, member))
        self.is_send(self.select_member, name)
        self.operation_element(self.select_member).send_keys(Keys.ENTER)
        self.is_click(self.select_confirm)
        self.is_click(self.str_conversion(self.confirm, 4))
        self.is_click(self.str_conversion(self.quick, '提交'))

    def get_table_text(self, location=3):
        """
        table的文字
        :param location:
        :return: 返回获取到的文字统计
        """
        return self.is_text(self.str_conversion(self.table, location))