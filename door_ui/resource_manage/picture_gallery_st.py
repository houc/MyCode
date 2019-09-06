import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from door_ui.resource_manage.currency import ResourceManagementElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestPictureGallery(UnitTests):
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
    def test_create_gallery_is_function_exist(self):
        """
        验证图片库上传一张新的图片对应模块是否存在
        1、产品管理{/managePanel/product/list/addOrEdit?appId=2&operType=add};
        2、企业图册{/managePanel/atlas/list/add?categoryId=&appId=4};
        3、图片库列表;
        4、内容介绍{/managePanel/introduce/list/addOrEdit}
        """
        try:
            driver = ResourceManagementElement(self.driver, self.toke_module)
            driver.get(self.url)
            is_exist = driver.gallery_exist()
            if is_exist:
                # 接口如果存在，那么再去web端验证是否也存在

                # ---------------这里是验证图片库列表是否存在UiAutoTests图片---------------
                driver.switch_window(1)  # 切换到Vue后台
                self.first = driver.gallery_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口存在UiAutoTests图片，但web界面中图片库列表却不存在UiAutoTests图片')

                # ---------------这里是验证产品管理是否存在UiAutoTests图片-----------------
                driver.get(f"{driver.interface.base_url}{self.data[0]}")
                self.first = driver.product_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口存在UiAutoTests图片，但web界面中添加产品上传附件却不存在UiAutoTests图片')

                # ---------------这里是验证企业图册是否存在UiAutoTests图片-----------------
                driver.get(f"{driver.interface.base_url}{self.data[1]}")
                self.first = driver.atlas_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口存在UiAutoTests图片，但web界面中添加企业图册上传附件却不存在UiAutoTests图片')

                # ---------------这里是验证内容介绍是否存在UiAutoTests图片-----------------
                driver.get(f"{driver.interface.base_url}{self.data[2]}")
                self.first = driver.content_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口存在UiAutoTests图片，但web界面中添加介绍内容上传附件却不存在UiAutoTests图片')

            else:
                # 如果不存在则新增附件
                driver.interface.upload_attr()

                # 上传成功后再次执行该用例
                return self.test_create_gallery_is_function_exist()
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_delete_gallery_is_function_exist(self):
        """
        验证图片库上传一张新的图片后又删除该图片对应模块是否存在
        1、产品管理{/managePanel/product/list/addOrEdit?appId=2&operType=add};
        2、企业图册{/managePanel/atlas/list/add?categoryId=&appId=4};
        3、图片库列表;
        4、内容介绍{/managePanel/introduce/list/addOrEdit}
        """
        try:
            driver = ResourceManagementElement(self.driver, self.toke_module)
            driver.get(self.url)
            is_exist = driver.gallery_exist()
            if not is_exist:
                # 接口如果存在，那么再去web端验证是否也存在

                # ---------------这里是验证图片库列表是否存在UiAutoTests图片---------------
                driver.switch_window(1)  #  切换到Vue后台
                self.first = driver.gallery_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口不存在UiAutoTests图片，但web界面中图片库列表却存在UiAutoTests图片')

                # ---------------这里是验证产品管理是否存在UiAutoTests图片-----------------
                driver.get(f"{driver.interface.base_url}{self.data[0]}")
                self.first = driver.product_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口不存在UiAutoTests图片，但web界面中添加产品上传附件却存在UiAutoTests图片')

                # ---------------这里是验证企业图册是否存在UiAutoTests图片-----------------
                driver.get(f"{driver.interface.base_url}{self.data[1]}")
                self.first = driver.atlas_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口不存在UiAutoTests图片，但web界面中添加企业图册上传附件却存在UiAutoTests图片')

                # ---------------这里是验证内容介绍是否存在UiAutoTests图片-----------------
                driver.get(f"{driver.interface.base_url}{self.data[2]}")
                self.first = driver.content_opera()
                self.screenshots = driver.screen_base64_shot()
                self.assertEqual(self.first, self.second,
                                 msg='图片库在接口不存在UiAutoTests图片，但web界面中添加介绍内容上传附件却存在UiAutoTests图片')

            else:
                # 如果存在则删除附件
                galley_set = driver.interface.delete_gallery()
                if galley_set:
                    # 使用接口删除的图片，已使用则判断是否为UiAutoTests图片
                    for gallery in galley_set:
                        get_name = gallery.get('gallery_name')
                        if get_name == 'UiAutoTests':
                            self.case_remark = '图片UIAutoTest已被使用，该用例未能执行'
                            break
                    else:
                        # 如不等于UiAutoTests则删除成功，再回到该用例重新运行
                        return self.test_delete_gallery_is_function_exist()

                else:
                    # 使用接口删除的图片，没有发现使用图片，则删除成功，再回到该用例重新运行
                    return self.test_delete_gallery_is_function_exist()

        except Exception:
            self.error = str(traceback.format_exc())
            raise
