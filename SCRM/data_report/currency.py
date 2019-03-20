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


class DataReportElement(OperationElement):
    """
    封装"DataReportElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.operation_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================url==========================================
    Add_Contacts_URL = MyYaml("SCRM").base_url + "/#/sale/contact"

    # ================================================元素==========================================

    company_and_self_switch = (By.XPATH, "(//div[starts-with(@class, 'ws-persission')])[$]")
    pie_in_data = (By.XPATH, "(//div[@class='header_tit'])[$]/div[1]/.")
    add_contacts_button = (By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[$]")
    input_button = (By.XPATH, "//div[contains(text(), '$')]/following::input[1]")
    message = (By.XPATH, "(//div[@class='ivu-message'])[$]/div/div/div/div/span")  # 消息提示框
    time_switch = (By.XPATH, "//div[@class='auto-width']/span[$]")  # 1:进30天，2:进三个月，3:近半年，4:近一年
    time_switch_display = (By.XPATH, "//div[@class='filter-result']/div/span")  # 选择的时间值
    custom_time = (By.XPATH, "(//input[starts-with(@class, 'ivu-input')])[$]")  # 1:开始时间， 2:结束时间
    select_time = (By.XPATH, "(//span[@class='ivu-date-picker-cells-cell'])[$]")  # 时间选择
    confirm = (By.XPATH, "//div[@class='fixed-width']/button[$]")  # 1:确定，2:取消
    select_pie = (By.XPATH, "(//div[starts-with(@class, 'ivu-select')])[$]/..")  # 图形中的下拉框选择，系统评级
    select_pie_content = (By.XPATH, "(//li[starts-with(@class, 'ivu-select')])[$]")  # 图形中的下拉框选择，具体选择的内容

    # ================================================强制等待时间==========================================

    create_wait_time = 2  # 创建对应功能后的等待时间
    assert_wait_time = 1  # 对应断言值的等待的时间

    def _in_class_attribute(self, element, location, text):
        """获取class属性值
        :param element: self.company_and_self_switch
        :param text: 对应属性值是否包含
        :return: 存在返回True，反之返回False
        """
        return self.is_attribute_class(self.str_conversion(element, location), text)

    def table_switch(self, value, text):
        """
        后去对应属性值
        :param value: 2:自己，3:公司
        :param text: 对应属性值是否包含
        :return:
        """
        time.sleep(self.assert_wait_time)
        return self._in_class_attribute(self.company_and_self_switch, value, text)

    def table_click(self, value):
        """
        自己和公司切换
        :param value: 2
        :return:
        """
        self.is_click(self.str_conversion(self.company_and_self_switch, value))

    def graphical_data(self, location):
        """
        图形中的饼型数据
        :param location: 位置
        :return: 返回对应数据值
        """
        time.sleep(self.create_wait_time)
        return self.is_text(self.str_conversion(self.pie_in_data, location))

    def add_contacts(self, location, text, content, save):
        """
        默认为添加联系人的方法
        :param location: 点击的位置，如新增联系人按钮是2
        :param text: 输入的内容，如:请输入邮箱
        :param content: 邮箱的内容
        :param save: 报错按钮，如6
        :return:
        """
        self.get(self.Add_Contacts_URL)
        self.is_click(self.str_conversion(self.add_contacts_button, location))
        self.operation_element(self.str_conversion(self.input_button, text)).send_keys(content)
        self.is_click(self.str_conversion(self.add_contacts_button, save))
        self.is_click(self.str_conversion(self.add_contacts_button, save), wait_time=4)

    def download_report(self, location, message_location):
        """
        下载报表
        :param location: 1
        :return: 对应数据
        """
        self.is_click(self.str_conversion(self.add_contacts_button, location))
        return self.is_text(self.str_conversion(self.message, message_location))

    def time_table(self, location):
        """
        时间选择切换
        :param location: # 1:进30天，2:进三个月，3:近半年，4:近一年
        :return:
        """
        self.is_click(self.str_conversion(self.time_switch, location))
        return self.is_text(self.time_switch_display)

    def custom_time_select(self, location=1):
        """
        自定义时间选择
        :param location:
        :return:
        """
        self.is_click(self.str_conversion(self.custom_time, 1))  # 点击开始时间
        self.is_click(self.str_conversion(self.select_time, 12))  # 选择时间
        self.is_click(self.str_conversion(self.custom_time, 2))  # 点击结束时间
        self.is_click(self.str_conversion(self.select_time, 55))  # 选择时间
        self.is_click(self.str_conversion(self.confirm, location))  # 确定

    def assert_time_selection(self):
        """
        时间默认选中的选项
        :return:
        """
        return self.is_text(self.time_switch_display)

    def pie_click(self, location):
        """
        图形中的系统评级下拉框选择
        :param location:
        :return:
        """
        self.is_click(self.str_conversion(self.select_pie, location))

    def pie_select(self, location):
        """
        图形中的系统评级下的选择内容
        :param location: 1:系统评级，2:生命周期，3:国家，4:来源
        :return:
        """
        self.is_click(self.str_conversion(self.select_pie_content, location))
        return self.is_attribute_class(self.str_conversion(self.select_pie_content, location),
                                       "ivu-select-item-selected")

