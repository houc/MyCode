import configparser

from config_path.path_file import one_level_catalog


class ConfigParameter(object):
    def __init__(self, dirName='BrowserToken.ini', encoding='utf-8'):
        """初始化"""
        self.path = one_level_catalog(dirName)
        self.encoding = encoding
        self.config = configparser.ConfigParser()

    def write_ini(self, content, node='session', child='token'):
        """将信息写入配置文件"""
        self.config.add_section(node)
        self.config.set(node, child, content)
        self.config.write(open(self.path, 'wt', encoding=self.encoding))

    def read_ini(self, node='session', child='token'):
        """读取配置文件中的信息"""
        self.config.read(self.path)
        ini = self.config.get(node, child)
        return {"token": ini}

