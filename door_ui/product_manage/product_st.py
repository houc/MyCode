import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from door_ui.product_manage.currency import ProductManageElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestProduct(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = True
    LOGIN_INFO = {"account": 'admin', "password": ' ', "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_product_is_exist(self):
        """
        验证后台增加产品前台是否存在，并且同时验证产品中的图片是否前台展示
        1、接口中如没有分类就新增分类{/managePanel/category/list/addOrEdite?appId=2};
        2、接口中如没有属性就新增属性{/managePanel/template/list/addOrEdit?id=&key=add&appId=2}
        3、接口中如没有产品就新增产品{/managePanel/product/list/addOrEdit?appId=2&operType=add}
        """
        # 请手动将产品属性管理的默认属性必填项隐藏掉，除开产品名称
        try:
            driver = ProductManageElement(self.driver)
            is_product_exist = driver.interface.search_product()
            is_class_exist = driver.interface.get_class()
            if is_class_exist:
                # 产品分类存在，校验产品是否存在
                if is_product_exist:
                    # 如果产品存在，则前端校验产品是否存在，以及产品下对应附件是否存在

                    # ---------------------接口存在该产品，在使用UI去判断是否存在---------------
                    driver.get(self.url)
                    driver.search_box(search_text='UI测试产品')
                    time.sleep(2)
                    self.first = driver.search_list_name_is_true(true_name='UI测试产品')
                    self.screenshots = driver.screen_base64_shot()
                    self.assertTrue(self.first, msg='接口存在“UI测试产品”，但web产品管理中没有存在')

                    # ------------进入前台验证-------------
                    driver.switch_window(0) # 切换到设计器tab
                    driver.design_create_template()
                    driver.design_drag()
                    driver.switch_window(2) # 切换到设计器预览窗口
                    time.sleep(2)
                    self.first = driver.views_opera()
                    self.second = list(is_product_exist[0].values())[0]
                    self.screenshots = driver.screen_base64_shot()
                    self.assertListEqual(self.first, self.second, msg='web端使用的图片在前台组件使用的图片不相等')

                    # ---------删除模板和产品-------------
                    driver.switch_window(0) # 切换到设计器tab
                    driver.designer_delete_page()
                    status = driver.interface.delete_product()
                    if status is not None:
                        self.assertTrue(status, msg='使用接口删除产品失败')
                else:
                    # 如果产品不存在，则添加产品
                    url = driver.interface.base_url + self.data[2]
                    driver.get(url)
                    self.first = driver.add_product()
                    self.second = '保存成功'
                    self.screenshots = driver.screen_base64_shot()
                    self.assertIsNotNone(self.first, msg='添加产品时，上传附件为空，请手动上传附件')
                    self.assertIn(self.second, self.first, msg='web端添加产品失败了')
                    return self.test_product_is_exist()
            else:
                # 如果分类不存在，则添加分类
                url = driver.interface.base_url + self.data[0]
                driver.get(url)
                self.first = driver.add_class()
                self.second = '保存成功'
                self.screenshots = driver.screen_base64_shot()
                self.assertIn(self.second, self.first, msg='web端添加分类失败了')
                return self.test_product_is_exist()
        except Exception:
            self.error = str(traceback.format_exc())
            raise

