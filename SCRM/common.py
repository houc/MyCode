import warnings
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
    account_and_password = (By.XPATH, "(//input[@class='mu-text-field-input'])[$]") # 账号和密码输入框
    login_button = (By.XPATH, "//button[@class='enabled']") # 登录按钮
    my_self = (By.XPATH, "//li[@class='user-profile']") # 个人信息是否存在

    def __init__(self, driver, account, password, company=None, *, module):
        BrowserToken.__init__(self, driver)
        self.account = account
        self.password = password
        self.company = company
        self.module = module
        self.url = MyConfig('url').base_url + '/#/account/login'

    def login(self, switch_toke=True):
        """登录：登录成功后是否需要获取token"""
        self.get(self.url)
        self.is_send(self.str_conversion(self.account_and_password, 1), self.account)
        self.is_send(self.str_conversion(self.account_and_password, 2), self.password)
        self.is_click(self.login_button)
        if self.is_element(self.my_self):
            if switch_toke:
                self.get_token()

    def get_token(self):
        """获取浏览器中的token"""
        js = "return window.localStorage.getItem('token')"
        token = self.execute_js(js)
        if token:
            token = json.loads(token)['val']
            self.config.write_ini(content=token, node=self.module)
        else:
            warnings.warn('获取浏览器token失败...')

    def remove_key(self):
        """从配置文件中删除写入的token值"""
        self.config.remove_node(self.module)

