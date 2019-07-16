CURRENCY_PY = '''import requests
import time

from model.Yaml import MyProject
from config_path.path_file import UP_FILE_NAME
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def read_currency(keys: str, line: int):
    """
    读取currency.ya中的数据
    Usage: 
        url = MyProject("SCRM").base_url + read_currency("get_customer", 0)
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


class {}(OperationElement):
    """
    封装"%s"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================\n

    # ================================================元素==========================================\n'''

CASE_CONTENT = '''import unittest
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from {} import {}

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class {}(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = False
    LOGIN_INFO = {{"account": None, "password": None, "company": None}}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

'''

CASE_NAME = '''    @test_re_runner(set_up)
    def {}(self):
        """
        {}
        """
        try:
            driver = {}(self.driver)
            driver.get(self.url)
            self.first = 
            self.screenshots = driver.screen_base64_shot()
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise\n
'''

CURRENCY_YA = '''#add_customer:
#  - url: /add/customerParam
#    bar: {name: 新增客户, address: 四川省成都市}'''

PROJECT_COMMON = '''import warnings
import json
import time

from model.GetToken import BrowserToken
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from model.Yaml import MyConfig

class LoginPublic(BrowserToken):
    """
    封装"LoginPublic"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text
    """
    # ================================================URL==========================================


    # ================================================元素==========================================

    def __init__(self, driver, account, password, company=None, *, module):
        BrowserToken.__init__(self, driver)
        self.account = account
        self.password = password
        self.company = company
        self.module = module

    def login(self, switch_toke=True):
        """登录：登录成功后是否需要获取token"""
        if switch_toke:
            self.get_token()

    def get_token(self):
        """获取浏览器中的token"""
        js = "return window.localStorage.getItem('token')"
        token = self.driver.execute_script(js)
        if token:
            token = json.loads(token)
            self.config.write_ini(content=token, node=self.module)
        else:
            warnings.warn('获取浏览器token失败...')

    def remove_key(self):
        """从配置文件中删除写入的token值"""
        self.config.remove_node(self.module)\n
'''


class GetTemplateHTML(object):
    def __init__(self, catalog, modules, level, method, address, scene, expect, actual, status, finish_time,
                 use_time, remark, id, members):
        self.catalog = catalog
        self.modules = modules
        self.level = level
        self.method = method
        self.address = address
        self.scene = scene
        self.expect = expect
        self.actual = actual
        self.status = status
        self.use_time = use_time
        self.finish_time = finish_time
        if 'None' == remark:
            self.remark = ''
        else:
            self.remark = 'data:image/JPEG;base64,' + remark
        self.id = id
        self.members = members

    def case_info(self):
        """用例详情"""
        return '''
    <div class="modal fade" id="{}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog popUp">
            <div class="modal-content">
                <div class="modal-header"><h4 class="modal-title" id="myModalLabel">{}详情</h4></div>
                <div class="modal-body">
                    <table class="popUp_table">
                        <tr>
                            <th class="th">目录:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">模块:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">用例级别:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">方法:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">地址:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">场景:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">预期结果:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">实际结果（异常原因）:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">状态:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">完成时间:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">用时:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">负责人:</th>
                            <td class="td"><pre class="is_p">{}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">附件:</th>
                            <td class='td'>
                                <img onclick="look_img_windows(this.src)" class="min" style="cursor: pointer" src='{}'>
                            </td>
                        </tr>
                    </table>
                </div>
                <div class="modal-footer" style="text-align: center">
                    <button type="button" class="btn btn-default" style="width: 15%;" data-dismiss="modal">关闭</button>
                </div>
            </div>
	    </div>
    </div>
        '''.format(self.method, self.method, self.catalog, self.modules,
                   self.level, self.method, self.address, self.scene,
                   self.expect, self.actual, self.status, self.finish_time, self.use_time,
                   self.members, self.remark)

    def case_list(self):
        """用例列表"""
        return '''
                        <tr>
                            <td class="list_td">{}</td>
                            <td class="list_td">{}</td>
                            <td class="list_td">{}</td>
                            <td class="list_td">{}</td>
                            <td class="list_td">{}</td>
                            <td class="list_td">{}</td>
                            <td class="list_td">{}</td>
                            <td class="list_td hand"><a data-toggle="modal" data-target="#{}">详细</a></td>
                        </tr>'''.format(self.catalog, self.modules, self.method, self.address,
                                        self.status, self.use_time, self.members, self.method)

    @property
    def _enlarge_img(self):
        return """<script>
        $(function(){
            $('#%s').click(function () {
                $(this).toggleClass('min');
                $(this).toggleClass('max')
            });
        });
    </script>
        """

    @property
    def _open_windows(self):
        return """<script>
        function look(content){
            if (content === "" || content === "None"){
                return false
        }
            else{
                var new_win = window.open();
                    new_win.document.write("<img src=" + content + " />")
        }

    }
    </script>
        """