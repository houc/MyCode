import requests
import dataclasses
import time
import json
import os

from model.Yaml import MyProject, MyConfig
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from model.MyException import InterfaceEqErrors
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def read_currency(keys: str, line: int):
    """
    读取currency.ya中的数据
    Usage: 
        url = MyConfig("door_ui").base_url + read_currency("get_customer", 0)
        data = read_currency("get_customer", 1)
    """
    data = []
    module = os.path.abspath(os.path.dirname(__file__)).split('\\')[-1]
    read = MyProject(module, keys).module_data
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]


def get_my_conf(section, option):
    """
    读取my_conf信息,section:获取的键，option获取的值键
    Usage:
        get_token = get_my_conf('user_msg', 'token')
        r = requests.post(url, headers={'token': get_token}, data=data, stream=True)
    """
    get_conf = ConfigParameter().read_ini(section, option)
    return get_conf
    

@dataclasses.dataclass
class InterfaceInterfaceAuxiliary(object):
    """
    用于接口辅助测试---->>>>所用到的对应功能接口方法集成类
    usage:
    def __init__(self):
        self.token = get_my_conf('Authentication', 'Authorization')
        .......................................................................
    
    def get_user_msg(self):
        data = read_currency('user_msg', 1)
        url = read_currency('user_msg', 0)
        .......................................................................
        
    """

    module: str

    def __post_init__(self):
        self.token = get_my_conf(self.module, 'token')  # 获取token
        self.tenantId = get_my_conf(self.module, 'tenantId')  # 获取租户Id
        self.design_cookie = get_my_conf('design_cookies', 'JSESSIONID')  # 设计器的session
        self.base_url = MyConfig('new_backstage').base_url  # 后台url
        self.design_url = MyConfig('designer').base_url  # 设计器url

    def request_except(self, r, module_name=None, remark=None,
                       back_data=None, except_status='-1', insert_data=None):
        """
        请求结果返回后异常处理封装，类似是否成功请求并成功返回对应状态码
        :param r: requests请求参数
        :param remark: 异常后备注
        :param module_name: 当前执行请求的模块名称
        :param back_data: 异常后返回的数据，如是html建议使用话术描述，不用完全返回，不然测试报告中存在太多，可能会引发异常！
        :param except_status: 异常后自定义一个状态码，请勿与判断状态码一致，否则执行下属代码会引发异常！
        :param insert_data: 传入数据
        :return: 元组返回，1为状态，2位异常值，用法：assert int(exception[0]) == 200, exception[1]
        """
        try:
            new_json = r.json()
            status = new_json.get('status')
            back_data = new_json
        except (json.JSONDecodeError, TypeError):
            status = except_status
            back_data = back_data
        exc = InterfaceEqErrors(
            module_name=module_name, status=r.status_code, url=r.url, type=r.request,
            used_time=r.elapsed.total_seconds(), back_data=back_data, remark=remark,
            insert_data=insert_data
        )
        return status, exc


class InterfaceElement(OperationElement):
    """
    封装"InterfaceElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.find_element(self.parametrization(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    # ================================================元素==========================================
    
    # ================================================初始化参数=====================================
    
    def __init__(self, driver):
        super(InterfaceElement, self).__init__(driver)
        self.interface = InterfaceInterfaceAuxiliary() # 继承接口类


