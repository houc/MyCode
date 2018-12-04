import yaml
from config_path.path_file import read_file

class MyYaml:
    def __init__(self,interface='ukuaiqi',encoding='utf-8'):
        """初始化参数"""
        self.interface = interface
        self.encoding = encoding

    @property
    def all_yaml(self):
        """读取config.yaml中全部参数"""
        path = read_file('config','config.yaml')
        f = open(path, encoding = self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def base_url(self):
        """获取yaml中base_url链接"""
        return self.all_yaml['base_url'][self.interface]

    @property
    def excel_parameter(self):
        """获取yaml中excel_parameter"""
        return self.all_yaml['excel_parameter'][self.interface]

    @property
    def config(self):
        """获取yaml中config"""
        return self.all_yaml['config'][self.interface]

if __name__ == '__main__':
    t = MyYaml('EDP').base_url
    print(t)