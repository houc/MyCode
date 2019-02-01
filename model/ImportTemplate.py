
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

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from model.SeleniumElement import ElementLocation

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class {}(UnitTests):\n'''

CASE_NAME = '''    def {}(self):
        """
        {}
        """
        try:
            self.level = {}
            self.author = {}
            self.urls = {!r}
            driver = ElementLocation(self.driver)
            driver.F5()
            driver.get(self.url + self.urls)
            %s
            self.second = {}
        except Exception as exc:
            self.error = str(exc)\n
'''


XPATH = '''driver.XPATH("{}")'''

CSS = '''driver.CSS("%s")'''

FIRST_ASSERT = '''self.first = %s'''

CURRENCY_YA = '''#add_customer:
#  - url: /add/customerParam
#    bar: {name: 新增客户, address: 四川省成都市}'''