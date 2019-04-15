from config_path.path_file import read_file
from model.Yaml import MyConfig

path = read_file(MyConfig('project_name').excel_parameter, 'token.ini')
with open(path, 'wt'):
    pass