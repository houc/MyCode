import warnings
import json

from model.GetToken import BrowserToken


class LoginPublic(BrowserToken):
    """
    封装"LoginPublic"元素类
    Usage:
        Demonstration = (By.XPATH, "(//span[text()='$'])[1]/.")

        def add_member(self, value):
            self.fin_element(self.str_conversion(self.Demonstration, value)).text

    # ================================================URL==========================================


    # ================================================元素==========================================
    """
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
        self.config.remove_node(self.module)