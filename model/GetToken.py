import json
import requests

from model.MyConfig import ConfigParameter
from model.Yaml import MyYaml


class BrowserToken(object):
    """
    该类主要用于获取浏览器中的token值
    """
    def __init__(self, driver):
        self.driver = driver
        self.write_ini = ConfigParameter().write_ini

    def get_token(self):
        """
        通过driver获取到driver中的token

        :return: 返回token值
        """
        js = "return window.localStorage.getItem('token')"
        token = self.driver.execute_script(js)
        self._write_token(token)

    def _write_token(self, token: str):
        """处理token样式后并将token写入到config.ini中"""
        if token is not None:
            conversion_token = json.loads(token)["val"]
            self.write_ini(child="Authorization", content=conversion_token)
        else:
            print("TOKEN未能在浏览器中获取成功，TOKEN写入失败")


class InterfaceModule:
    """
    该模块主要用于UI测试时，需调用接口测试的辅助测试
    """
    def __init__(self, modules: classmethod):
        """
        初始化

        :arg: self.requests初始化成一个实例
        :arg: self.url截取成: https://www.scrm365.cn
        """
        self.requests = requests.session()
        self.read_ini = ConfigParameter().read_ini
        self.module = modules

    @staticmethod
    def read_common(parameter: str, line: int) -> str or int:
        """读取currency.ya文件函数"""
        data = []
        all_read = MyYaml(interface=parameter).readCommon
        for read in all_read:
            data.append(read['url'])
            data.append(read['bar'])
        if isinstance(line, int):
            return data[line]
        else:
            raise TypeError("line参数错误")

    @property
    def token(self):
        """读取认证"""
        token_keys = MyYaml('token_keys').config
        return {token_keys: self.read_ini(child='authorization')}


if __name__ == '__main__':
    print(BrowserToken(''))
