import os
import time
import asyncio

from model.Yaml import MyYaml

async def check_token():
    """检查token是否失效"""
    path = os.path.dirname(__file__)
    invalid_time = MyYaml('token_invalid').config
    current_file = os.listdir(path)
    ini = [i for i in current_file if '.ini' in i][0]
    login = [i for i in current_file if 'Login.py' in i][0]
    path_ini = path + '/{}'.format(ini)
    getmtime = os.path.getmtime(path_ini)
    current_time = time.time()
    result_time = (current_time - getmtime) / 3600
    if result_time >= invalid_time:
        run_path = os.path.join(path, login).replace('\\', '/')
        os.system(run_path)

loop = asyncio.get_event_loop()
loop.run_until_complete(check_token())
