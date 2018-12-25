import configparser
import requests

from config_path.path_file import read_file
from model.Yaml import MyYaml
from model.MyException import RequestsError, FUN_NAME


class _ConfigParameter(object):
    def __init__(self, dir='IsEDP', dirName='config.ini', encoding='utf-8'):
        """初始化"""
        self.path = read_file(dir, dirName)
        self.encoding = encoding
        self.config = configparser.ConfigParser()

    def write_ini(self, content, node='session', child='token'):
        """将信息写入配置文件"""
        self.config.add_section(node)
        self.config.set(node, child, content)
        self.config.write(open(self.path, 'w', encoding=self.encoding))

    def read_ini(self, node='session', child='token'):
        """读取配置文件中的信息"""
        self.config.read(self.path)
        _ini = self.config.get(node, child)
        return {"token": _ini}


class GetToken(_ConfigParameter):
    def __init__(self, keys='Login'):
        """初始化"""
        super(GetToken, self).__init__()
        self.account = MyYaml('account').config
        self.password = MyYaml('password').config
        self.login_url = MyYaml(keys).parameter_interface['url']

    def login(self):
        """请求登录并将token写入配置文件中"""
        url = MyYaml('EDP_Interface').base_url + self.login_url
        data = {"loginName": self.account, "password": self.password}
        r = requests.post(url, data=data)
        if r.json().get('code') == 0:
            tokens = r.json().get('model').get('tokens')
            self.write_ini(tokens)
            return self.read_tokens()
        else:
            raise RequestsError(FUN_NAME(), r.json())

    def read_tokens(self):
        """读取token"""
        return self.read_ini()

if __name__ == '__main__':
    print(GetToken().login())