
CURRENCY_PY = '''import requests

from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter

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
    return token\n'''


CASE_CONTENT = '''import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation

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
            driver = ElementLocation(self.driver)
            driver.get(self.url)
            driver.F5()
            %s
        except Exception as exc:
            self.error = str(exc)\n
'''


# XPATH = '''driver.XPATH("{}")'''
#
# CSS = '''driver.CSS("%s")'''

# FIRST_ASSERT = '''time.sleep(1)
#             self.driver.save_screenshot(self.screenshots_path)
#             self.first = %s'''

ELEMENT = '''driver.element_handle(self.element)
            time.sleep(1)
            self.driver.save_screenshot(self.screenshots_path)
            self.first = driver.element_handle(self.get_asserts, switch=True)'''

CURRENCY_YA = '''#add_customer:
#  - url: /add/customerParam
#    bar: {name: 新增客户, address: 四川省成都市}'''