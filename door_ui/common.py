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
    backstage_url = MyConfig('new_backstage').base_url
    
    # ================================================元素==========================================
    # --------设计器元素----------
    account_element = (By.NAME, "username") # 账号
    password_element = (By.NAME, "password") # 密码
    domain_element = (By.NAME, "domain") # 地址
    submit_element = (By.TAG_NAME, "button") # 提交按钮
    my_self = (By.XPATH, "//li[contains(@class, 'jumpNewManager')]") # 登录成功后断言是否新后台元素加载出来

    #------新后台元素--------
    backstage_element = (By.XPATH, "//div[contains(@class, 'resource rel')]") # 资源包
    login_quit = (By.ID, "fm1") # 检查新后台token是否失效
    username_ele = (By.ID, "username") # 新后台登录账户元素
    password_ele = (By.ID, "password") # 新后台登录密码元素
    immediately = (By.CLASS_NAME, "immediately") # 新后台登录按钮的元素
    is_login_success = (By.CLASS_NAME, "firstLevel") # 判断是否成功登录新后台

    def __init__(self, driver, account, password, backstage=backstage_url, module=None):
        BrowserToken.__init__(self, driver)
        self.account = account
        self.password = password
        self.backstage = backstage
        self.module = module
        self.url = MyConfig('designer').base_url

    def login_design(self, psw=False):
        """登录设计器：登录成功后是否需要获取token"""
        self.get(self.url)
        self.send_keys(self.account_element, self.account)
        if psw:
            self.send_keys(self.password_element, self.password)
        self.send_keys(self.domain_element, self.backstage)
        self.submit(self.submit_element)
        assert self.is_element(self.my_self), '设计器登录失败！'
        self._get_design()
        self.get_token()

    def get_token(self):
        """获取浏览器中的token"""
        time.sleep(8)
        self.set_attributed(self.my_self, 'style', ' ')
        self.click(self.backstage_element)
        self.click(self.my_self)
        self.switch_window(-1)
        self.get(self.backstage_url + '/managePanel/product/list?appId=2') # 验证登录新后台后token是否失效（访问产品管理）
        if self.quick_is_element(self.login_quit):
            self.login_backstage()
        else:
            self._get_backstage_token()

    def _get_design(self):
        # 后去设计器cookie，并写入配置文件中
        cookie = self.driver.get_cookie('JSESSIONID').get('value')
        self.config.remove_section(section='design_cookies')
        self.config.add_section(section='design_cookies')
        self.config.set(section='design_cookies', option='JSESSIONID', value=cookie)
        self.config.write_ini()

    def _get_backstage_token(self):
        # 获取新后台token
        js_token = "return window.sessionStorage.getItem('token')"
        js_tenantId = "return window.sessionStorage.getItem('tenantId')"
        token = self.execute_js(js_token)
        tenantId = self.execute_js(js_tenantId)
        print(token, tenantId)
        if token is not None and tenantId is not None:
            self.config.remove_section(section=self.module)
            self.config.add_section(section=self.module)
            self.config.set(section=self.module, option='token', value=token)
            self.config.set(section=self.module, option='tenantId', value=tenantId)
            self.config.write_ini()

    def login_backstage(self):
        # 登录新后台
        account = MyConfig('backstage_user').base_url
        password = MyConfig('backstage_password').base_url
        self.send_keys(self.username_ele, account)
        self.send_keys(self.password_ele, password)
        self.submit(self.immediately)
        assert self.quick_is_element(self.is_login_success), '新后台登录失败！'
        self._get_backstage_token()

    def remove_token(self, keys):
        # 移除token
        self.config.remove_node(keys)


if __name__ == '__main__':
    from model.DriverParameter import browser
    driver = browser()
    try:
        login = LoginPublic(driver=driver, account='admin', password=None, module='backstage_token')
        login.login_design()
    except: raise
    finally: driver.quit()
