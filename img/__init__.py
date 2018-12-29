import os
import requests
import asyncio

from model.Yaml import MyYaml
from model.MyException import RequestsError, FUN_NAME
from config_path.path_file import read_file
from PIL import Image

async def get_log():
    """获取项目logo"""
    url = MyYaml('EDP').base_url + MyYaml('logo_url').config
    log_path = read_file('img', 'logo.png')
    r = requests.get(url, stream=True)
    with open(log_path, 'wb') as f:
        f.write(r.content)
    if os.path.exists(log_path):
        img = Image.open(log_path)
        x, y = img.size
        p = Image.new('RGBA', img.size, (255, 255, 255))
        p.paste(img, (0, 0, x, y), img)
        p.save(log_path)
    else:
        raise RequestsError(FUN_NAME(), '未能获取到logo')

async def current_file_path():
    """获取当前路径下所有的文件名，并删除以test_开头的png"""
    path = os.path.dirname(__file__)
    paths = os.listdir(path)
    for i in paths:
        if 'test_' in i:
            path = read_file('img', i)
            os.remove(path)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([current_file_path(), get_log()]))
