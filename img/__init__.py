import requests
import os

from model.Yaml import MyYaml
from config_path.path_file import read_file
from PIL import Image

def get_log():
    """获取项目logo"""
    url = MyYaml('EDP').base_url + MyYaml('logo_url').config
    log_path = read_file('img','logo.png')
    r = requests.get(url)
    with open(log_path,'wb') as f:
        f.write(r.content)
        f.close()
    if os.path.exists(log_path):
        img = Image.open(log_path)
        x,y = img.size
        p = Image.new('RGBA',img.size,(255,255,255))
        p.paste(img, (0,0,x,y),img)
        p.save(log_path)

def current_file_path(path='.'):
    """获取当前路径下所有的文件名，并删除以test_开头的png"""
    paths = os.listdir(path)
    for i in paths:
        if 'test_' in i:
            _path = read_file('img',i)
            os.remove(_path)

if __name__ == '__main__':
    get_log()
    current_file_path()