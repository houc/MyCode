import configparser
import os

from model.Yaml import MyYaml


class ConfigParameter(object):
    def __init__(self, dirName='/BrowserToken.ini', encoding='utf-8'):
        """初始化"""
        self.path = os.path.realpath(os.path.dirname(os.path.dirname(__file__))) + dirName
        self.encoding = encoding
        self.config = configparser.ConfigParser()
        self.keys = MyYaml('token_keys').config

    def write_ini(self, content, node='session'):
        """将信息写入配置文件"""
        self.config.add_section(node)
        self.config.set(node, self.keys, content)
        self.config.write(open(self.path, 'wt', encoding=self.encoding))

    def read_ini(self, node='session'):
        """读取配置文件中的信息"""
        self.config.read(self.path)
        ini = self.config.get(node, self.keys)
        return {self.keys: ini}

if __name__ == '__main__':
    h = ConfigParameter().read_ini()
    print(h)
