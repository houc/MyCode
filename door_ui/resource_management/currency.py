import requests
import time
import json
import os
import dataclasses

from model.Yaml import MyConfig, MyProject
from model.MyConfig import ConfigParameter
from model.MyException import InterfaceEqErrors
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
    module = os.path.abspath(os.path.dirname(__file__)).split('\\')[-1]
    read = MyProject(module, keys).module_data
    for i in read:
        data.append(i['url'])
        data.append(i['bar'])
    return data[line]


def token(section, option):
    """
    获取token值,module:获取的值
    Usage:
        r = requests.post(url, headers=token(module), data=data, stream=True)
    """
    get_token = ConfigParameter().read_ini(section, option)
    return get_token


@dataclasses.dataclass
class GalleryInterfaceAuxiliary(object):
    """
    用于接口辅助测试---->>>>所用到的对应功能接口方法集成类
    """
    gallery_ids = list()  # 图片库列表搜索出来的图片对应信息

    def __post_init__(self):
        self.token = token('new_token', 'token') # 获取token
        self.tenantId = token('new_token', 'tenantId') # 获取租户Id

    def request_except(self, r, module_name='图片库列表搜索',  remark=None,
                       back_data='接口错误或token失效，无法访问！', except_status='-1'):
        """
        请求结果返回后异常处理封装，类似是否成功请求并成功返回对应状态码
        :param r: requests请求参数
        :param remark: 异常后备注
        :param module_name: 当前执行请求的模块名称
        :param back_data: 异常后返回的数据，如是html建议使用话术描述，不用完全返回，不然测试报告中存在太多，可能会引发异常！
        :param except_status: 异常后自定义一个状态码，请勿与判断状态码一致，否则执行下属代码会引发异常！
        :return: 元组返回，1为状态，2位异常值，用法：assert int(exception[0]) == 200, exception[1]
        """
        try:
            new_json = r.json()
            status = new_json.get('status')
            back_data = new_json
        except TypeError:
            status = except_status
            back_data = back_data
        exc = InterfaceEqErrors(
            module_name=module_name, status=r.status_code, url=r.url, type=r.request,
            used_time=r.elapsed.total_seconds(), back_data=back_data, remark=remark
        )
        return status, exc

    def search_gallery(self):
        # 通过接口访问，图片库是否存在test图片，存在则返回存在当前页面40条数据图片id，该接口在其他列表中会重复使用（banner、产品）
        # 传入的数据处理

        # 访问的url处理
        url = (MyConfig('new_backstage').base_url +
               read_currency('search_gallery_is_exits', 0)) % (self.tenantId, self.token)

        # 开始请求并处理请求后的结果
        r = requests.get(url=url, stream=True, timeout=10)
        exception = self.request_except(r)
        assert int(exception[0]) == 200, exception[1] # 断言执行请求状态是否为200
        gallery_ids = json.loads(r.json().get('data')).get('data').get('list')
        if gallery_ids: # 判断图片是否存在
            for gallery_id in gallery_ids:
                id = gallery_id.get('id')
                class_name = gallery_id.get('appName')
                name = gallery_id.get('name')
                used = gallery_id.get('used')
                self.gallery_ids.append({
                    'gallery_id': id,
                    'class_name': class_name,
                    'gallery_name': name,
                    'used': used
                })
        else: # 如不存在则返回一个bool为False
            return False
        return self.gallery_ids

    def delete_gallery(self):
        # 通过接口删除搜索出来的图片，已使用图片不处理删除
        gallery_set = self.search_gallery() # 搜索图片名称为test开头图片
        register_used = [] # 寄存已使用的图片信息
        if gallery_set: # test是否存在
            # 循环处理删除
            for ids in gallery_set:
                # 删除接口url的信息处理
                id = ids.get('gallery_id')
                used = ids.get('used')
                if used != 1: # 判断图片是否被使用，1已使用；0未使用
                    url = (MyConfig('new_backstage').base_url +
                           read_currency('delete_gallery', 0)) % (id, self.tenantId, self.token)
                    r = requests.get(url=url, stream=True, timeout=10)
                    exception = self.request_except(r)
                    assert int(exception[0]) == 200, exception[1] # 断言执行请求状态是否为200
                else:
                    register_used.append(ids)
        return register_used # 返回已使用图片信息

    def upload_attr(self):
        # 上传附件为图片，上传成功后返回当前成功的图片名和图片id
        # 上传附件url
        url = (MyConfig('new_backstage').base_url +
               read_currency('upload_msg', 0)) % (self.tenantId, self.token)

        # 处理data
        data = read_currency('upload_msg', 1)

        file_path = f'{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}/img/test.jpeg'
        file = {'file': open(file_path, 'rb')}
        r = requests.post(url=url, files=file, data=data, timeout=10, stream=True)
        exception = self.request_except(r)
        assert int(exception[0]) == 200, exception[1]  # 断言执行请求状态是否为200
        data = json.loads(r.json().get('data')).get('data')
        return {'gallery_id': data.get('id'),
                'gallery_name': data.get('name')}


class ResourceManagementElement(OperationElement):
    """
    封装"ResourceManagementElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.")

        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    # ================================================元素==========================================
    def __init__(self, driver):
        super(ResourceManagementElement, self).__init__(driver)
        self.interface = GalleryInterfaceAuxiliary() # 集成接口类





if __name__ == '__main__':
    con = InterfaceAuxiliary()
    k = con.upload_attr()
    print(k)