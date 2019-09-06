import requests
import dataclasses
import time
import json
import os

from model.Yaml import MyProject, MyConfig
from model.MyConfig import ConfigParameter
from model.MyException import InterfaceEqErrors
from door_ui.resource_manage.currency import ResourceManagementElement
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


def get_my_conf(section, option):
    """
    读取my_conf信息,section:获取的键，option获取的值键
    Usage:
        get_token = get_my_conf('user_msg', 'token')
        r = requests.post(url, headers={'token': get_token}, data=data, stream=True)
    """
    get_conf = ConfigParameter().read_ini(section, option)
    return get_conf
    

@dataclasses.dataclass
class ProductManageInterfaceAuxiliary(object):
    """
    用于接口辅助测试---->>>>所用到的对应功能接口方法集成类
    usage:
    def __init__(self):
        self.token = get_my_conf('Authentication', 'Authorization')
        .......................................................................
    
    def get_user_msg(self):
        data = read_currency('user_msg', 1)
        url = read_currency('user_msg', 0)
        .......................................................................
        
    """
    module: str

    def __post_init__(self):
        self.token = get_my_conf(self.module, 'token')  # 获取token
        self.tenantId = get_my_conf(self.module, 'tenantId')  # 获取租户Id
        self.design_cookie = get_my_conf('design_cookies', 'JSESSIONID')  # 设计器的session
        self.base_url = MyConfig('new_backstage').base_url  # 后台url
        self.design_url = MyConfig('designer').base_url  # 设计器url

    def request_except(self, r, module_name=None, remark=None,
                       back_data=None, except_status='-1', insert_data=None):
        """
        请求结果返回后异常处理封装，类似是否成功请求并成功返回对应状态码
        :param r: requests请求参数
        :param remark: 异常后备注
        :param module_name: 当前执行请求的模块名称
        :param back_data: 异常后返回的数据，如是html建议使用话术描述，不用完全返回，不然测试报告中存在太多，可能会引发异常！
        :param except_status: 异常后自定义一个状态码，请勿与判断状态码一致，否则执行下属代码会引发异常！
        :param insert_data: 传入数据
        :return: 元组返回，1为状态，2位异常值，用法：assert int(exception[0]) == 200, exception[1]
        """
        try:
            new_json = r.json()
            status = new_json.get('status')
            back_data = new_json
        except (json.JSONDecodeError, TypeError):
            status = except_status
            back_data = back_data
        exc = InterfaceEqErrors(
            module_name=module_name, status=r.status_code, url=r.url, type=r.request,
            used_time=r.elapsed.total_seconds(), back_data=back_data, remark=remark,
            insert_data=insert_data
        )
        return status, exc

    def search_product(self, product_name='UI测试产品', asserts='eq'):
        # 产品列表搜索产品
        url = (self.base_url + read_currency('search_product_is_exits', 0)) % (self.tenantId, self.token)
        production = [] # 通过接口获取产品的对应信息
        data = read_currency('search_product_is_exits', 1)
        data['keyword'] = product_name
        r = requests.post(url=url, json=data, timeout=10, stream=True)
        exception = self.request_except(r, module_name='产品列表搜索产品', insert_data=data)
        assert int(exception[0]) == 200, exception[1]  # 断言执行请求状态是否为200
        data = json.loads(r.json().get('data')).get('data').get('list')
        if not data: # 接口中如不存在产品，返回一个bool为False
            return False
        else:
            img_urls = []
            for product in data:

                def search():  # 查找产品方法
                    product_id = product.get('id')
                    product_img_urls = product.get('productImages')
                    if product_img_urls is not None:    # 判断产品中是否有图片
                        for product_img_url in product_img_urls:
                            img_url = product_img_url.get('thumbUrl')
                            img_urls.append(img_url)
                    if img_urls:   # 如果产品中有产品附件，那么与产品对应id和附件信息一并添加到产品列表中
                        production.append({
                            product_id: img_urls
                        })
                        return production
                    else: # 如果没有产品附件，返回产品id到产品列表
                        production.append(product_id)

                if asserts == 'eq':
                    if product.get('productName') == product_name:
                        return search()
                if asserts == 'in_eq':
                    if product_name in product.get('productName'):
                        search()
            else:
                if not production: return False

        return list(map(int, production))


    def delete_product(self, product_name='UI测试产品', asserts='eq'):
        # 删除产品
        del_id = self.search_product(product_name=product_name, asserts=asserts)

        def del_product(prod_id):
            url = (self.base_url + read_currency('delete_product', 0)) % (prod_id, self.tenantId, self.token)
            r = requests.get(url=url, stream=True, timeout=10)
            exception = self.request_except(r, module_name='删除产品')
            assert int(exception[0]) == 200, exception[1]  # 断言执行请求状态是否为200
            data = json.loads(r.json().get('data')).get('data').get('success') # 返回产品状态bool值，这个是在接口中获取的！
            return data

        for __del in del_id:
            if isinstance(__del, dict):
                ids = list(__del.keys())[0]
                return del_product(ids) # 返回删除状态

            elif isinstance(__del, int):
                del_status = del_product(__del)
                if not del_status: return False

        else: return None # 没有需要删除的产品

    def get_class(self, class_type='这是一个顶级分类测试'):
        # 获取分类
        url = (self.base_url + read_currency('get_class', 0)) % (self.tenantId, self.token)
        r = requests.get(url=url, stream=True, timeout=10)
        class_manage = [] #  分类管理数据
        exception = self.request_except(r, module_name='获取产品分类')
        assert int(exception[0]) == 200, exception[1]  # 断言执行请求状态是否为200
        data = json.loads(r.json().get('data')).get('data')
        if not data: return False # 接口中如不存在分类，返回一个bool为False
        else:
            for __class in data:
                id = __class.get('id')
                name = __class.get('categoryName')
                if name == class_type:
                    class_manage.append({
                        'id': id,
                        'name': name
                    })
                    break
            else: return False
        return class_manage

    def get_attribute(self, attribute='测试规格属性值'):
        # 获取属性管理
        url = (self.base_url + read_currency('get_attribute', 0)) % (self.tenantId, self.token)
        r = requests.get(url=url, stream=True, timeout=10)
        attribute_manage = []  # 属性管理数据
        exception = self.request_except(r, module_name='获取产品属性管理')
        assert int(exception[0]) == 200, exception[1]  # 断言执行请求状态是否为200
        data = json.loads(r.json().get('data')).get('data').get('list')
        if not data:
            return False  # 接口中如不存在分类，返回一个bool为False
        else:
            for __attribute in data:
                id = __attribute.get('id')
                name = __attribute.get('templateName')
                if name == attribute:
                    attribute_manage.append({
                        'id': id,
                        'name': name
                    })
                    break
            else:
                return False
        return attribute_manage

    def interface_import_product(self):
        # 接口导入产品
        url = (self.base_url + read_currency('import_product', 0)) % (self.tenantId, self.token)
        data = read_currency('import_product', 1)
        product_file = f'{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}/img/ProductData.zip'
        file = {'file': open(product_file, 'rb')}
        r = requests.post(url=url, files=file, timeout=10, data=data, stream=True)
        exception = self.request_except(r, module_name='导入产品', insert_data=data)
        assert int(exception[0]) == 200, exception[1]  # 断言执行请求状态是否为200
        result = r.json().get('message')
        return result  # 获取导入返回的信息


class ProductManageElement(ResourceManagementElement):
    """
    封装"ProductManageElement"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.find_element(self.parametrization(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    # ================================================元素==========================================

    # -----------设计器模板-----------
    message = (By.XPATH, "(//i[contains(@class,'si icon-addpages')])[1]")  # 信息架构
    new = (By.XPATH, "//input[contains(@class,'btn gray normal t-input shadow')]")  # 新建
    new_page = (By.XPATH, "//li[@class='selectPageType']")  # 空白页面
    PX = (By.XPATH, "//h3[text()='响应布局']/parent::li")  # 响应布局模式
    PX_name = (By.XPATH, "//input[@data-bind='value: pageInfo.name']")  # 输入名称
    save = (By.XPATH, "//button[text()='创建']")  # 保存创建
    delete_name = (By.XPATH, "//span[@class='displayPageName' and text()='$']/parent::div/..") # 定位创建成功的模板名
    tips_delete = (By.XPATH, "//div[starts-with(@class, 'dialog panel pop ui-draggable')]") # 删除弹出
    delete_button = (By.XPATH, "//div[@class='$']/div/div[3]/div[2]/button")  # 弹窗中的删除确定按钮

    # ---------设计器拖拽-----------
    function_unit = (By.XPATH, "//i[contains(@class,'si icon-components')]")  # 功能组件
    list_search = (By.XPATH, "(//div[@class='new-search-button'])[1]")  # 列表搜索按钮
    send = (By.XPATH, "(//div[@class='new-search'])[1]/input")  # 输入框
    page_search = (By.XPATH, "(//div[@class='new-search'])[1]/button")  # 页面搜索按钮
    units = (By.XPATH, "//ul[@id='itemlist']/li/h3")  # 搜索出来结果一组要拖拽的组件
    unit = (By.XPATH, '(//*[@id="itemlist"]/li/img)[$]') # 定位需要拖拽组件
    close = (By.XPATH, "(//span[@class='close'])[5]/a/i")  # 关闭组件弹窗
    page_save = (By.XPATH, "//div[text()='保存']") # 保存配置模板
    view = (By.XPATH, "//div[text()='预览']") # 预览模板

    # --------设计器预览------------
    views_time = (By.XPATH, "//div[contains(@class, 'js_PUBLISH_TIME')]") # 发布时间排序
    all_img = (By.XPATH, "//div[@data-target='_parent']/a[1]/div/img") # 多张产品
    get_img_url = (By.XPATH, "(//div[@data-target='_parent'])[$]/a") # 产品下多张图片

    # ---------添加产品-------------
    input_box = (By.XPATH, "(//input[@class='el-input__inner'])[$]") # 产品输入框
    send_product_classify = (By.XPATH, "//div[contains(@class,'tagBox')]")  # 点击分类
    class_text = (By.XPATH, "//span[@class='el-tree-node__label']") # 多个分类名字
    select_class = (By.XPATH, "(//span[@class='el-tree-node__label'])[$]/preceding-sibling::label") # 选择获取的类
    attribute_type = (By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[$]/li[$]") # 属性类型
    upload_attr = (By.XPATH, "(//div[@class='addImgItem'])[$]") # 上传附件
    select_attr = (By.XPATH, "(//div[@class='listCon'])/div/div") # 选择附件
    ok = (By.XPATH, "(//span[text()='确 定'])[7]/parent::button") # 附件确定
    button = (By.XPATH, "//span[text()='保存']/parent::button") # 保存按钮
    tips_box = (By.XPATH, "//div[@role='alert']/p") # 弹窗消息

    # ------设计器预览界面获取产品id--------
    views_product_id = (By.CLASS_NAME, "e_box.p_Product")  # 获取多个产品class名

    # -------添加分类----------

    # ================================================初始化参数=====================================
    
    def __init__(self, driver, module):
        super(ProductManageElement, self).__init__(driver, module)
        self.interface = ProductManageInterfaceAuxiliary(module) # 继承接口类

    def design_create_template(self):
        # 设计器创建模板
        time.sleep(2)
        self.is_click(self.message)
        time.sleep(2)
        self.is_click(self.new)
        time.sleep(1)
        self.is_click(self.new_page)
        time.sleep(1)
        self.is_click(self.PX)
        time.sleep(1)
        self.send_keys(self.PX_name, 'UI自动化测试模板')
        time.sleep(1)
        self.is_click(self.save)
        time.sleep(5)

    def design_drag(self, unit_name='产品列表通用'):
        # 设计器拖拽
        time.sleep(2)
        self.is_click(self.function_unit)
        time.sleep(2)
        self.is_click(self.list_search)
        time.sleep(2)
        self.send_keys(self.send, unit_name)
        time.sleep(1)
        self.is_click(self.page_search)
        time.sleep(1)
        is_elements = self.is_elements(self.units)
        if is_elements:
            for count, element in enumerate(is_elements, start=1):
                if element.text == unit_name:
                    transfer = self.parametrization(self.unit, count)
                    self.drag_and_drop_by_offset(transfer, 700, 100)
                    time.sleep(3)
                    self.is_click(self.close)
                    time.sleep(1)
                    self.is_click(self.page_save)
                    time.sleep(2)
                    self.is_click(self.view)
                    time.sleep(2)
                    break
            else: return False # 如果未找到就返回false
        else: return False # 如果未找到就返回false

    def designer_delete_page(self):
        # 测试结束删除新增页面，需要先切回设计器地址
        self.is_click(self.message)
        transfer = self.parametrization(self.delete_name, 'UI自动化测试模板')
        elements = self.is_elements(transfer)
        if elements:
            for element in elements:
                time.sleep(5)
                element.click()
                time.sleep(4)
                current_element = element.get_attribute('class')
                delete = (By.XPATH,
                          f"//li[@class='{current_element}']/div[2]/div/i[3]")  # 定位页面删除按钮
                time.sleep(2)
                self.is_click(delete)
                time.sleep(2)
                is_none = self.is_elements(self.tips_delete)
                if is_none:
                    for is_element in is_none:
                        none = is_element.get_attribute('class')
                        if 'aui_state_focus' in none:
                            transfer1 = self.parametrization(self.delete_button, none)  # 弹窗中的删除
                            self.is_click(transfer1)

    def views_opera(self, product_name='UI测试产品'):
        # 预览操作，需要先切换到预览界面
        self.is_click(self.views_time)
        time.sleep(3)
        elements = self.is_elements(self.all_img)
        img_urls = []
        if elements:
            for count, element in enumerate(elements, start=1):
                name = element.get_attribute('title')
                if name == product_name:
                    transfer = self.parametrization(self.get_img_url, count)
                    urls = self.is_elements(transfer)
                    for url in urls:
                        new = url.get_attribute('imghref')
                        img_urls.append(new)
                    return img_urls
            else: return False # 如果没有该产品就返回false
        else: return False # 如果没有该产品就返回false

    def views_get_product_id(self):
        # 在设计器预览界面，获取产品
        product_id = []
        self.is_click(self.views_time)
        time.sleep(3)
        elements = self.is_elements(self.views_product_id)
        if not elements:
            return False
        else:
            for element in elements:
                time.sleep(0.5)
                data_id = element.get_attribute('dataid')
                product_id.append(data_id)  # 返回设计器预览界面中的从id 在源码中的e_box p_Product->dataid获取
            return list(map(int, product_id))

    def add_product(self):
        # 添加产品
        transfer = self.parametrization(self.input_box, 2) # 产品名称
        self.send_keys(transfer, 'UI测试产品')
        time.sleep(1)
        self.is_click(self.send_product_classify)
        time.sleep(1)
        elements = self.is_elements(self.class_text)
        if not elements: return False # 如果没有分类返回false
        else:
            for count, element in enumerate(elements, start=1):
                if element.text == '这是一个顶级分类测试':
                    transfer1 = self.parametrization(self.select_class, count)
                    self.is_click(transfer1)
                    time.sleep(1)
                    self.is_click(transfer)
                    time.sleep(1)
                    transfer2 = self.parametrization(self.input_box, 4)
                    self.is_click(transfer2)
                    transfer3 = self.parametrization(self.attribute_type, 4, 1)
                    self.is_click(transfer3)
                    time.sleep(1)
                    transfer4 = self.parametrization(self.upload_attr, 2)
                    self.is_click(transfer4)
                    time.sleep(1)
                    attr_elements = self.is_elements(self.select_attr)
                    if not attr_elements:
                        return None
                    for count, attr_element in enumerate(attr_elements, start=1):
                        attr_element.click()
                        if count > 2: break
                    self.is_click(self.ok)
                    time.sleep(1)
                    self.is_click(self.button)
                    time.sleep(1)
                    return self.get_text(self.tips_box)
            else: return False

    def add_class(self):
        # 添加分类
        transfer = self.parametrization(self.input_box, 3)  # 分类名称
        self.send_keys(transfer, '这是一个顶级分类测试')
        time.sleep(1)
        self.is_click(self.button)
        time.sleep(1)
        return self.get_text(self.tips_box)

    def search_box(self, search_text='UI测试产品导入'):
        super(ProductManageElement, self).search_box(search_text=search_text)

    def search_list_name_is_true(self, true_name='UI测试产品导入', asserts='in_eq'):
        # 产品列表中搜索产品
        return super(ProductManageElement, self).search_list_name_is_true(true_name=true_name,
                                                                          asserts=asserts)

if __name__ == '__main__':
    k = ProductManageInterfaceAuxiliary('backstage_token').search_product('UI测试产品导入', 'in_eq')
    print(k)
