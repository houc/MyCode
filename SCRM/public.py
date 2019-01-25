
from model.SeleniumElement import ElementLocation
from model.GetToken import BrowserToken


class LoginTestModules(object):
    # ======================================元素==================================================================== #

    account_element = '手机号/邮箱*/../input!!send'
    password_element = '密码*/../input!!send'
    login_element = '登录*!!click'
    company_element = '请选择要登录的公司*/../../div[2]/div/div/div/ul/li[1]!!click'
    assert_success = '超人*/../span[1]!!text'
    is_open = '找回密码*/../a!!text'

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url + '/#/account/login'

    def success_login(self, account, password):
        """登录成功"""
        self.driver.get(self.url)
        element = ElementLocation(self.driver)
        element.XPATH(self.account_element, account)
        element.XPATH(self.password_element, password)
        element.XPATH(self.login_element)
        element.XPATH(self.company_element)
        assert element.XPATH(self.assert_success) == "超人"
        BrowserToken(self.driver).get_token()

    def opens_if(self):
        """网址是否打开"""
        self.driver.get(self.url)
        element = ElementLocation(self.driver)
        assert element.XPATH(self.is_open) == "找回密码"
