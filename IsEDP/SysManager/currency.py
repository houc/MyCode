
from model.Yaml import MyYaml
from config_path.path_file import UP_FILE_NAME


def read_public(keys, line):
    """读取public.yaml中的数据"""
    _data = []
    read = MyYaml(UP_FILE_NAME).ModulePublic[keys]
    for i in read:
        _data.append(i['url'])
        _data.append(i['bar'])
    return _data[line]



