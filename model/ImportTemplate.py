import dataclasses
import time

__author__ = 'hc'

CURRENCY_PY = '''import requests
import time
import json
import os

from model.Yaml import MyProject, MyConfig
from model.MyConfig import ConfigParameter
from model.SeleniumElement import OperationElement
from model.MyException import InterfaceEqErrors
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
    module = os.path.abspath(os.path.dirname(__file__)).split('\\\\')[-1]
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
        r = requests.post(url, headers={{'token': get_token}}, data=data, stream=True)
    """
    get_conf = ConfigParameter().read_ini(section, option)
    return get_conf


class {}InterfaceAuxiliary(object):
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


class {}(OperationElement):
    """
    封装"%s"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.") 

        def add_member(self, value):
            self.find_element(self.parametrization(self.Demonstration, value)).text
    """
    # ================================================URL==========================================

    # ================================================元素==========================================

    # ================================================初始化参数=====================================

    def __init__(self, driver):
        super({}, self).__init__(driver)
        self.interface = {}InterfaceAuxiliary() # 继承接口类\n\n'''

CASE_CONTENT = '''import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner, case_self_monitor
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
        driver = {}(self.driver)
        driver.get(self.url)
        self.first = 
        self.screenshots = driver.screen_base64_shot()
        self.assertEqual(self.first, self.second)

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


@dataclasses.dataclass
class GetTemplateHTML(object):
    case_catalog: str
    case_module: str
    case_level: str
    case_name: str
    case_url: str
    case_scene: str
    case_results: str
    case_error_reason: str
    case_insert_parameter: str
    status: str
    insert_time: time
    case_wait_time: time
    case_author: str
    case_img: str
    case_remark: str

    def __post_init__(self):
        if 'None' == self.case_img: self.url = ''
        else: self.url = 'data:image/JPEG;base64,' + self.case_img
        if 'None' == self.case_url: self.case_url, self.td_url = '', None
        else: self.td_url = ''

    def case_info(self):
        """用例详情"""
        if self.url: img_url = f'''<img onclick="look_img_windows(this.src)" class="min" style="cursor: pointer" src='{self.url}'>'''
        else: img_url = ''
        return f'''
    <div class="modal fade" id="{self.case_name}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog popUp">
            <div class="modal-content">
                <div class="modal-header"><h4 class="modal-title" id="myModalLabel">{self.case_name}详情</h4></div>
                <div class="modal-body">
                    <table class="popUp_table">
                        <tr>
                            <th class="th">目录:</th>
                            <td class="td"><pre class="is_p">{self.case_catalog}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">模块:</th>
                            <td class="td"><pre class="is_p">{self.case_module}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">用例级别:</th>
                            <td class="td"><pre class="is_p">{self.case_level}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">方法:</th>
                            <td class="td"><pre class="is_p">{self.case_name}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">地址:</th>
                            <td class="td">
                                <pre class="is_p"><a target="_blank" href="{self.case_url}">{self.case_url}</a>{None if self.td_url is None else self.td_url}</pre>
                            </td>
                        </tr>
                        <tr>
                            <th class="th">场景:</th>
                            <td class="td"><pre class="is_p">{self.case_scene}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">预期结果:</th>
                            <td class="td"><pre class="is_p">{self.case_results}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">实际结果（异常原因）:</th>
                            <td class="td"><pre class="is_p">{self.case_error_reason}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">传入参数:</th>
                            <td class="td"><pre class="is_p">{self.case_insert_parameter}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">状态:</th>
                            <td class="td"><pre class="is_p">{self.status}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">完成时间:</th>
                            <td class="td"><pre class="is_p">{self.insert_time}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">用时:</th>
                            <td class="td"><pre class="is_p">{self.case_wait_time}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">负责人:</th>
                            <td class="td"><pre class="is_p">{self.case_author}</pre></td>
                        </tr>
                        <tr>
                            <th class="th">附件:</th>
                            <td class='td'>{img_url}</td>
                        </tr>
                        <tr>
                            <th class="th">备注:</th>
                            <td class="td"><pre class="is_p">{self.case_remark}</pre></td>
                        </tr>
                    </table>
                </div>
                <div class="modal-footer" style="text-align: center">
                    <button type="button" class="btn btn-default" style="width: 15%;" data-dismiss="modal">关闭</button>
                </div>
            </div>
	    </div>
    </div>
        '''

    def case_list(self):
        """用例列表"""
        return f'''
                        <tr>
                            <td class="list_td">{self.case_catalog}</td>
                            <td class="list_td">{self.case_module}</td>
                            <td class="list_td">{self.case_name}</td>
                            <td class="list_td"><a target="_blank" href="{self.case_url}">{self.case_url}</a>{None if self.td_url is None else self.td_url}</td>
                            <td class="list_td">{self.status}</td>
                            <td class="list_td">{self.case_wait_time}</td>
                            <td class="list_td">{self.case_author}</td>
                            <td class="list_td hand"><a data-toggle="modal" data-target="#{self.case_name}">详细</a></td>
                        </tr>'''

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