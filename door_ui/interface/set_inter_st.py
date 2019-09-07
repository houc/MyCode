import unittest
import requests
import json
import zipfile
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.TimeConversion import standard_time, custom_sub_time
from model.SkipModule import Skip, current_module
from door_ui.interface.currency import InterfaceInterfaceAuxiliary

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class InterfaceSet(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = False
    BROWSER = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_visit_statistics(self):
        """
        验证openapi访问统计是否正常
        """
        interface = InterfaceInterfaceAuxiliary('backstage_token')
        self.url = self.url % interface.tenantId
        r = requests.get(url=self.url, stream=True, timeout=10)
        self.first = r.json().get('msg')
        self.assertEqual(self.first, self.second, msg=r.content.decode())

    @test_re_runner(set_up)
    def test_WeChat(self):
        """
        使用接口验证openapi微信
        """
        interface = InterfaceInterfaceAuxiliary('backstage_token')
        self.url = self.url % interface.tenantId
        r = requests.get(url=self.url, stream=True, timeout=10)
        self.first = r.json().get('msg')
        self.assertEqual(self.first, self.second)

    @test_re_runner(set_up)
    def test_Redis(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        interface = InterfaceInterfaceAuxiliary('backstage_token')
        self.url = self.url % interface.tenantId
        r = requests.get(url=self.url, stream=True, timeout=10)
        self.first = r.json().get('code')
        self.assertEqual(self.first, self.second)

    @test_re_runner(set_up)
    def test_prod_export(self):
        """
        导出产品，是否成功
        1、使用导出产品接口，是否成功，默认为当前时间前一月
        """
        interface = InterfaceInterfaceAuxiliary('backstage_token')
        tenant_id = interface.tenantId
        token = interface.token
        start_time = custom_sub_time(30).replace(' ', '+')[:-3]
        end_time = standard_time().replace(' ', '+')[:-3]

        self.url = self.url % (start_time, end_time, tenant_id, token)
        init_data = self.data[0].replace("'", '"')
        data = json.loads(init_data)
        data['startDate'] = start_time
        data['endDate'] = end_time
        self.data = data

        response = requests.get(url=self.url, stream=True, timeout=10, data=self.data)
        response.raise_for_status()
        download_file = f'{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}/img/product_data.zip'
        with open(download_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=10000):  # 边下边存
                file.write(chunk)

        with zipfile.ZipFile(download_file) as files:
            for file in files.namelist():
                self.first = file
                self.assertEqual(self.first, self.second, msg='导出产品失败，zip的products.xlsx不存在')


