import requests
import time
import json

from model.Yaml import MyConfig, MyProject
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def read_currency(keys: str, line: int):
    """
    读取currency.ya中的数据
    Usage: 
        url = MyConfig("door_ui").base_url + read_currency("get_customer", 0)
        data = read_currency("get_customer", 1)
    """
    data = []
    read = MyProject(UP_FILE_NAME, keys).module_data
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]


def token(module):
    """
    获取token值,module:获取的值
    Usage:
        r = requests.post(url, headers=token(module), data=data, stream=True)
    """
    return ConfigParameter().read_ini(node=module)


class ResourceManagementElement():
    """
    封装"ResourceManagementElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    # ================================================元素==========================================
    gallery_ids = [] # 图片库列表搜索出来的图片对应信息

    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


    def search_gallery(self):
        # 通过接口访问，图片库是否存在test图片，存在则返回存在当前页面40条数据图片id
        # 传入的数据处理
        data = read_currency('search_gallery_is_exits', 1)
        data.update(token('new_token'))

        # 访问的url处理
        url = (MyConfig('new_backstage').base_url +
               read_currency('search_gallery_is_exits', 0)) % data.get('new_token')

        # 开始请求并处理请求后的结果
        r = requests.get(url=url, headers=self.headers, data=data, stream=True, timeout=10)
        assert r.status_code == 200, f'图片库搜索图片接口异常，访问连接为:{url}，访问时间为:{r.elapsed.total_seconds()}秒！'
        gallery_ids = json.loads(r.json().get('data')).get('data').get('list')
        if gallery_ids:
            for gallery_id in gallery_ids:
                print(gallery_id)
                id = gallery_id.get('id')
                class_name = gallery_id.get('appName')
                name = gallery_id.get('name')
                used = gallery_id.get('used')
                self.gallery_ids.append({
                    'gallery_id': id, #图片id
                    'class_name': class_name, # #当前图片所在分类
                    'gallery_name': name, #图片名称
                    'used': used #是否使用，1已使用，0未使用
                })
        return self.gallery_ids







if __name__ == '__main__':
    ResourceManagementElement().search_gallery()