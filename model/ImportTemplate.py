
CURRENCY_PY = '''import requests
import time

from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import ElementLocation
from selenium.webdriver.common.by import By

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


class {}(ElementLocation):
    """
    封装"%s"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 
        
        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """

    # ================================================元素==========================================\n'''

CASE_CONTENT = '''import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from . currency import {}

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class {}(UnitTests):
    """
    当RE_LOGIN = True即为需要重新登录，或者是需要切换账号登录，当RE_LOGIN为True时，需要将LOGIN_INFO的value值全填写完成，
    如果请求的账号中只有一家公司那么company中的value就可以忽略不填写，否则会报错...
    MODULE为当前运行的模块
    """
    RE_LOGIN = False
    LOGIN_INFO = {{"account": None, "password": None, "company": None}}
    MODULE = os.path.dirname(__file__).split("\\\\")[-1]
    
'''

CASE_NAME = '''    def {}(self):
        """
        {}
        """
        try:
            driver = {}(self.driver)
            driver.get(self.url)
            driver.F5()
            # 操作元素.....
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
        except Exception as exc:
            self.error = str(exc)\n
'''


# XPATH = '''driver.XPATH("{}")'''
#
# CSS = '''driver.CSS("%s")'''

# FIRST_ASSERT = '''time.sleep(1)
#             self.driver.save_screenshot(self.screenshots_path)
#             self.first = %s'''


CURRENCY_YA = '''#add_customer:
#  - url: /add/customerParam
#    bar: {name: 新增客户, address: 四川省成都市}'''