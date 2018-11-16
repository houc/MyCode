import yaml
from cofpath.path_file import get_config_yaml_path

class MyYaml:
    def __init__(self,interface='interface',encoding='utf-8',url='project_url'):
        """初始化参数"""
        self.interface = interface
        self.encoding = encoding
        self.url = url

    @property
    def read_all_yaml(self):
        """读取config.yaml中全部参数"""
        path = get_config_yaml_path()
        f = open(path, encoding = self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def read_test_config(self):
        """读取test_login.yaml中的全部参数"""
        path = get_config_yaml_path()
        f = open(path, encoding = self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def read_interface(self):
        """获取yaml中的interface数据"""
        a = MyYaml().read_all_yaml
        return a[self.interface]

    @property
    def base_url(self):
        """获取yaml中url链接"""
        a = MyYaml().read_interface
        return a[self.url]

    @property
    def read_interface_app(self):
        """获取read_test_config.yaml中的interface数据"""
        a = MyYaml().read_test_config
        return a[self.interface]



if __name__ == '__main__':
    t = MyYaml().read_interface
    print(t)