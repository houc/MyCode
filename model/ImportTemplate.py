
CURRENCY_PY = '''
from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME

def read_currency(keys, line):
    """读取currency.ya中的数据"""
    data = []
    read = MyYaml(UP_FILE_NAME).ModulePublic[keys]
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]
'''


CASE_CONTENT = '''import unittest

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import {}

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class {}(UnitTests):  
'''

CASE_NAME = '''    def {}(self):
        """
        {}
        """
        try:
            self.level = {}
            self.author = {}
            elements = {}(self.driver, self.url)
            self.first = elements.{}(self.urls)
            self.second = {}
        except Exception as exc:
            self.error = str(exc)
            
'''

MAIN = '''if __name__ == '__main__':
    unittest.main()'''