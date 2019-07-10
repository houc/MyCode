import configparser

from model.Yaml import MyConfig
from config_path.path_file import read_file


class ConfigParameter(object):
    def __init__(self, dirName='token.ini', encoding='utf-8'):
        """初始化"""
        self.project = MyConfig('project_name').excel_parameter
        self.path = read_file(self.project, dirName)
        self.encoding = encoding
        self.config = configparser.ConfigParser()
        self.keys = MyConfig('token_keys').config

    def write_ini(self, content, node='session'):
        """将信息写入配置文件"""
        self.config.add_section(node)
        self.config.set(node, self.keys, content)
        with open(self.path, 'at', encoding=self.encoding) as f:
            self.config.write(f)

    def read_ini(self, node='session'):
        """读取配置文件中的信息"""
        self.config.read(self.path)
        ini = self.config.get(node, self.keys)
        return {self.keys: ini}

    def remove_node(self, node='session'):
        """删除不用的session"""
        self.config.read(self.path)
        self.config.remove_section(node)
        with open(self.path, 'wt', encoding=self.encoding) as f:
            self.config.write(f)

    def clear(self):
        """清除配置文件的全部信息"""
        self.config.clear()
        with open(self.path, 'wt', encoding=self.encoding) as f:
            self.config.write(f)


if __name__ == '__main__':
    cf = ConfigParameter()

