import yaml

from config_path.path_file import read_file, module_file


class MyConfig(object):
    def __init__(self, query_key, encoding='utf8'):
        self.query_key = query_key
        self.encoding = encoding

    @property
    def _read_config_data(self):
        path = read_file('config', 'conf.yaml')
        with open(path, 'rt', encoding=self.encoding) as f:
            return yaml.safe_load(f)

    @property
    def base_url(self):
        return self._read_config_data['base_url'][self.query_key]

    @property
    def excel_parameter(self):
        return self._read_config_data['excel_parameter'][self.query_key]

    @property
    def report(self):
        return self._read_config_data['report'][self.query_key]

    @property
    def config(self):
        return self._read_config_data['config'][self.query_key]

    @property
    def send_email(self):
        return self._read_config_data['send_email'][self.query_key]

    @property
    def sql(self):
        return self._read_config_data['sql'][self.query_key]


class MyProject(object):
    def __init__(self, module, query_key='', encoding='utf8'):
        self.query_key = query_key
        self.module = module
        self.encoding = encoding
        self.pro_name = MyConfig('project_name').excel_parameter

    @property
    def _read_project_data(self):
        path = read_file(self.pro_name, 'common.yaml')
        with open(path, 'rt', encoding=self.encoding) as f:
            return yaml.safe_load(f)

    @property
    def parameter_ui(self):
        return self._read_project_data[self.pro_name]

    @property
    def module_data(self):
        return self._read_pro_module_data[self.query_key]

    @property
    def _read_pro_module_data(self):
        path = module_file(self.pro_name, self.module, 'currency.yaml')
        with open(path, 'rt', encoding=self.encoding) as f:
            return yaml.safe_load(f)


if __name__ == '__main__':
    y = MyProject('').parameter_ui
    print(y['home'])