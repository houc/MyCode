import os
import time

from model.Yaml import MyYaml
from IsEDP.InterfaceLogin import GetToken

def check_token():
    """检查token是否失效"""
    invalid_time = MyYaml('token_invalid').config
    path = os.path.dirname(__file__)
    current_file = os.listdir(path)
    ini = [i for i in current_file if '.ini' in i][0]
    path = path + '/{}'.format(ini)
    getmtime = os.path.getmtime(path)
    current_time = time.time()
    result_time = (current_time - getmtime) / 3600
    if result_time >= invalid_time:
        GetToken().login()

check_token()

