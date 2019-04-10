
CURRENCY_PY = '''import requests
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


class {}(OperationElement):
    """
    封装"%s"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================\n
    
    # ================================================元素==========================================\n'''

CASE_CONTENT = '''import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.SkipModule import Skip, current_module
from {} import {}

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class {}(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {{"account": None, "password": None, "company": None}}
    MODULE = os.path.abspath(__file__)
    
'''

CASE_NAME = '''    def {}(self):
        """
        {}
        """
        try:
            driver = {}(self.driver)
            driver.get(self.url)
            
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())\n
'''

CURRENCY_YA = '''#add_customer:
#  - url: /add/customerParam
#    bar: {name: 新增客户, address: 四川省成都市}'''

PROJECT_COMMON = '''from model.GetToken import BrowserToken


class LoginPublic(BrowserToken):
    """
    封装"LoginPublic"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text

    # ================================================URL==========================================

    
    # ================================================元素==========================================
    """
    def __init__(self, driver, account, password, company=None, *, module):
        BrowserToken.__init__(self, driver)
        self.account = account
        self.password = password
        self.company = company
        self.module = module

    def login(self, switch_toke=True):
        """登录：登录成功后是否需要获取token"""
        if switch_toke:
            self.get_token()

    def get_token(self):
        """获取浏览器中的token"""
        js = "return window.localStorage.getItem('token')"
        token = self.driver.execute_script(js)
        if token:
            token = json.loads(token)
            self.config.write_ini(content=token, node=self.module)
        else:
            warnings.warn('获取浏览器token失败...')

    def remove_key(self):
        """从配置文件中删除写入的token值"""
        self.config.remove_node(self.module)\n
'''