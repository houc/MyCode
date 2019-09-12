import configparser

from . Yaml import MyConfig
from config_path.path_file import read_file


class _MyConfigParse(configparser.ConfigParser):

    def optionxform(self, option_str):
        return option_str


class ConfigParameter(object):
    def __init__(self, dirName='my_conf.ini', encoding='utf-8'):
        """初始化"""
        self.project = MyConfig('project_name').excel_parameter
        self.path = read_file(self.project, dirName)
        self.encoding = encoding
        self.config = _MyConfigParse()

    def write_ini(self):
        """将信息写入配置文件"""
        with open(self.path, 'wt', encoding=self.encoding) as f:
            self.config.write(f)

    def set(self, section, option, value=None):
        """
        调用该方法时，需要先保证.ini中存在section
        :param section: [这是值]
        :param option: 变量名
        :param value: 变量值
        :usage

            conf = ConfigParameter()
            conf.add_section('user_messages')
            conf.set('user_messages', 'account', 'admin')
            conf.set('user_messages', 'password', '123456')
            conf.set('user_messages', 'age', '32岁')
            conf.set('user_messages', 'sex', '白富美哦')
            conf.set('user_messages', 'stature', '细长')
            conf.write_ini()

        """
        self.config.set(section, option, value)

    def add_section(self, section):
        """添加值section[这是值]"""
        self.config.add_section(section)

    def read_ini(self, section, option, raw=False, vars=None, fallback=object()):
        """读取配置文件中的信息"""
        self.config.read(self.path, encoding=self.encoding)
        content = self.config.get(section, option, raw=raw, vars=vars, fallback=fallback)
        return content

    def remove_section(self, section='session'):
        """删除不用的section"""
        self.config.read(self.path, encoding=self.encoding)
        self.config.remove_section(section)
        with open(self.path, 'wt', encoding=self.encoding) as f:
            self.config.write(f)

    def remove_option(self, section, option):
        # 移除不用的section下的option
        self.config.read(self.path, encoding=self.encoding)
        self.config.remove_option(section, option)
        with open(self.path, 'wt', encoding=self.encoding) as f:
            self.config.write(f)

    def clear(self):
        """清除配置文件的全部信息"""
        self.config.clear()
        with open(self.path, 'wt', encoding=self.encoding) as f:
            self.config.write(f)


if __name__ == '__main__':
    conf = ConfigParameter()
    conf.remove_option('user_messages', 'age')
