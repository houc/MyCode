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
    module: str

    def __post_init__(self):
        self.token = token('backstage_token', 'token') # 获取token
        self.tenantId = token(self.module, 'tenantId') # 获取租户Id
        self.design_cookie = token(self.module, 'JSESSIONID') # 设计器的session
        self.base_url = MyConfig('new_backstage').base_url # 后台url
        self.design_url = MyConfig('designer').base_url # 设计器url

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
        url = (self.base_url + read_currency('search_gallery_is_exits', 0)) % (self.tenantId, self.token)

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
                img_href = gallery_id.get('imgUrl')
                self.gallery_ids.append({
                    'gallery_id': id,
                    'class_name': class_name,
                    'gallery_name': name,
                    'used': used,
                    'img_href': img_href
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
                    url = (self.base_url + read_currency('delete_gallery', 0)) % (id, self.tenantId, self.token)
                    r = requests.get(url=url, stream=True, timeout=10)
                    exception = self.request_except(r)
                    assert int(exception[0]) == 200, exception[1] # 断言执行请求状态是否为200
                else:
                    register_used.append(ids)
        return register_used # 返回已使用图片信息

    def upload_attr(self):
        # 上传附件为图片，上传成功后返回当前成功的图片名和图片id
        # 上传附件url
        url = (self.base_url + read_currency('upload_msg', 0)) % (self.tenantId, self.token)

        # 处理data
        data = read_currency('upload_msg', 1)

        file_path = f'{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}/img/UiAutoTests.jpeg'
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

    views_switch = (By.XPATH, "//div[@role='radiogroup']/label[$]") # 视图切换 1为列表视图；2为缩略视图
    search = (By.XPATH, "//input[@placeholder='输入后直接回车确认']") # 搜索框搜索
    list_data = (By.XPATH, "//tr[starts-with(@class, 'el-table__row')]") # 列表数据
    get_list_name = (By.XPATH, "(//tr[starts-with(@class, 'el-table__row')])[$]/td[$]")  # 列表视图对应名称 参数1函数，参数2列数
    add_attr = (By.XPATH, "(//div[@class='addImgItem'])[$]") # 点击产品界面中的上传图片按钮
    select_classification = (By.XPATH, "(//div[@class='el-select type el-select--small'])/div") # 选择图片中的分类栏
    select_value = (By.XPATH, "(//div[@class='el-scrollbar'])[$]/div[1]/ul/li[$]") # 分类选项中的值
    attr_search = (By.XPATH, "//div[@class='listCon']/div/div[$]/div[2]") # 获取添加附件弹窗中的附件名
    attr_is_exist = (By.CLASS_NAME, "noFileList") # 获取添加附件弹窗中的附件是否为空
    attr_lists = (By.XPATH, "//div[@class='listCon']/div/div") # 获取添加附件弹窗中的附件总数

    def __init__(self, driver, module):
        super(ResourceManagementElement, self).__init__(driver)
        self.interface = GalleryInterfaceAuxiliary(module) # 集成接口类

    def gallery_exist(self):
        # 检查图片图片是否存在
        is_exist = self.interface.search_gallery() # 使用接口去搜索test图片是否存在
        if not is_exist: # 如果不存在则返回bool为False
            return False
        else: # 如果存在则返回bool为True
            return True

    def search_box(self, search_text='UiAutoTests'):
        # 列表搜索框搜索对应内容
        # search_text: 搜索的内容
        self.send_keys(self.search, search_text)  # 列表中输入搜索内容
        self.opera_element(self.search).send_keys(Keys.ENTER)  # 执行点击搜索按钮

    def search_list_name_is_true(self, true_name='UiAutoTests'):
        # 通过搜索出来的内容进行遍历查出对应附件名是否存在
        # true_name: 图片库图片名称
        elements = self.is_elements(self.list_data)
        if not elements:
            return False

        for element in range(len(elements)):
            transfer = self.parametrization(self.get_list_name, (element + 1), 3)
            text = self.get_text(transfer)
            if true_name == text:
                return True
        else:
            return False

    def gallery_opera(self):
        # 图片库列表操作图片是否存在
        transfer = self.parametrization(self.views_switch, 1)
        time.sleep(5) # 等待图片库列表渲染时间
        self.is_click(transfer)
        time.sleep(1)
        self.search_box()
        time.sleep(1)
        return self.search_list_name_is_true()

    def product_opera(self):
        # 产品管理添加图片是否存在
        return self.__upload_attr()

    def atlas_opera(self):
        # 企业图册添加图片是否存在
        return self.__upload_attr(attr=1, select_vale=3)

    def content_opera(self):
        # 介绍内容添加图片是否存在
        return self.__upload_attr(attr=1, select_vale=4)

    def __upload_attr(self, attr=2, select_vale=6):
        # 上传附件操作
        time.sleep(5) # 进入点击/编辑界面等待渲染时间
        transfer1 = self.parametrization(self.add_attr, attr)
        self.is_click(transfer1)
        time.sleep(1)
        self.is_click(self.select_classification)
        time.sleep(0.5)
        transfer = self.parametrization(self.select_value, select_vale, 1)
        self.is_click(transfer)
        time.sleep(1)
        self.search_box()
        time.sleep(1)
        return self.__attr_data_search()

    def __attr_data_search(self, true_name='UiAutoTests'):
        # 附件列表搜索出来后查找附件是否存在
        elements = self.is_elements(self.attr_lists)
        if not elements:
            return False

        for element in range(len(elements)):
            transfer = self.parametrization(self.attr_search, (element + 1))
            text = self.get_text(transfer)
            if true_name == text:
                return True
        else:
            return False



if __name__ == '__main__':
    con = GalleryInterfaceAuxiliary()
    k = con.get_attribute()
    print(k)