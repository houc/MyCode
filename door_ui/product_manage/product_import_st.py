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
class TestProductImport(UnitTests):
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
    def test_product_import(self):
        """
        导入产品，是否成功
        1、接口查找导入产品是否存在{/manager/gwforward/manager-webapi/product/productInformation/list}
        """
        driver = ProductManageElement(self.driver, self.toke_module)
        driver.get(self.url)
        self.second = driver.interface.search_product(product_name='UI测试产品导入', asserts='in_eq')
        if self.second and isinstance(self.second, list):
            # 接口中存在产品，并且产品中不包含产品附件
            driver.switch_window(1)  # 切换到Vue后台
            driver.search_box()
            time.sleep(2)
            self.first = driver.search_list_name_is_true()
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(len(self.first), len(self.second), msg='产品列表-搜索产品接口查询出来的产品数量与web查询出来的结果数量不一致,'
                                                                    '请收到查看导入记录，如导入记录不存在，则该产品导入失败，检查属性管理'
                                                                    '是否与导入模板属性一致！')

            # ------------进入前台验证导入产品是否存在-------------
            driver.switch_window(0)  # 切换到设计器tab
            time.sleep(2)
            driver.design_create_template()
            driver.design_drag()
            driver.switch_window(2)  # 切换到设计器预览窗口
            time.sleep(2)
            self.first = driver.views_get_product_id()
            self.screenshots = driver.screen_base64_shot()
            driver.close_current_window()

            for eq in self.second:
                self.assertIn(eq, self.first, msg='导入产品-接口中产品id与设计器预览id不一致')

            # ---------删除模板和产品-------------
            driver.switch_window(0)  # 切换到设计器tab
            time.sleep(2)
            driver.designer_delete_page()
            status = driver.interface.delete_product(product_name='UI测试产品导入', asserts='in_eq')
            if status is not None:
                self.assertTrue(status, msg='使用接口删除产品失败')

        if not self.first:
            import_status = driver.interface.interface_import_product()
            time.sleep(6)  # 执行导入后，默认等待6秒执行
            self.assertTrue(import_status, msg='产品列表中无产品时，使用接口导入产品失败')
            return self.test_product_import()

