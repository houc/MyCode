import os
import requests

from model.Yaml import MyYaml
from model.Thread import ExecuteThread
from config_path.path_file import read_file
from PIL import Image

def get_log():
    """获取项目logo"""
    url = MyYaml('SCRM').base_url + MyYaml('logo_url').config
    r = requests.get(url, stream=True)
    if r.content:
        log_path = read_file('img', 'logo.png')
        with open(log_path, 'wb') as f:
            f.write(r.content)
        if os.path.exists(log_path):
            img = Image.open(log_path)
            x, y = img.size
            p = Image.new('RGBA', img.size, (255, 255, 255))
            p.paste(img, (0, 0, x, y), img)
            p.save(log_path)

def current_file_path():
    """获取当前路径下所有的文件名，并删除以test_开头的png"""
    path = os.path.dirname(__file__)
    paths = os.listdir(path)
    for i in paths:
        if 'test_' in i:
            path = read_file('img', i)
            os.remove(path)

ExecuteThread(method=[current_file_path, get_log]).run()

