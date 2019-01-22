import yaml

from config_path.path_file import read_file, module_file


class MyYaml(object):
    def __init__(self,interface='SCRM', encoding='utf-8'):
        """初始化参数"""
        self.interface = interface
        self.encoding = encoding

    @property
    def AllConfig(self):
        """读取config.yaml中全部参数"""
        path = read_file('config', 'config.yaml')
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def AllPublic(self):
        """读取public.yaml中的全部参数"""
        path = read_file('SCRM', 'common.yaml')
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def ModulePublic(self):
        """读取测试模块下的public全部参数"""
        path = module_file(self.interface, 'currency.yaml')
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def Parameter(self):
        """Parameter.yaml中的全部参数"""
        path = read_file('SCRM', 'common.yaml')
        f = open(path, encoding=self.encoding)
        data = yaml.load(f)
        f.close()
        return data

    @property
    def parameter_ui(self):
        """读取公共参数UI信息"""
        return self.Parameter['SCRM']

    @property
    def parameter_interface(self):
        """读取公共参数接口信息"""
        return self.Parameter['Interface'][self.interface]

    @property
    def base_url(self):
        """获取yaml中base_url链接"""
        return self.AllConfig['base_url'][self.interface]

    @property
    def excel_parameter(self):
        """获取yaml中excel_parameter"""
        return self.AllConfig['excel_parameter'][self.interface]

    @property
    def config(self):
        """获取yaml中config"""
        return self.AllConfig['config'][self.interface]

    @property
    def send_email(self):
        """邮件发送配置参数"""
        return self.AllConfig['send_email'][self.interface]

    @property
    def sql(self):
        """读取sql参数"""
        return self.AllConfig['sql'][self.interface]

if __name__ == '__main__':
    t = MyYaml('Logins').parameter_ui
    print(t)
