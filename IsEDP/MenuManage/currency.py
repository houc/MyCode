
from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME

def read_currency(keys, line):
    """读取currency.ya中的数据"""
    data = []
    read = MyYaml(UP_FILE_NAME).ModulePublic[keys]
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]
