import time
import requests

from IsEDP.Elements import DriverTransmit
from selenium.webdriver.common.keys import Keys


class LoginModule(DriverTransmit):
    def success_login(self, account, password):
        """成功登陆"""
        asserts = self._asserts()
        assert asserts == '登录'
        self.xpathS('el-input__inner')[0].send_keys(account)
        self.xpathS('el-input__inner')[1].send_keys(password)
        self.xpath('btn-login').click()
        time.sleep(2)
        assert self.xpathS('user')[1].text == '欢迎您！用户'

    def opens_if(self):
        """判断网址是否打开"""
        asserts = self._asserts()
        assert asserts == '登录'


class MenuModule(DriverTransmit):
    def _menu(self, url):
        """菜单的公共方法"""
        self.driver.get(self.url + url)

    def CreateMenuNull(self, url):
        """创建菜单名称为空"""
        self._menu(url)
        self.xpathS('新增', 'text()')[0].click()
        self.xpathS('确认', 'text()')[1].click()
        self.asserts = self.xpathS('el-notification__content')[0].text


class LoginModules(DriverTransmit):
    def _login(self, url):
        """登录公共方法"""
        self.driver.get(self.url + url)

    def _clearInput(self):
        """清除用户名和密码中的内容"""
        self.xpathS('el-input__inner')[0].send_keys(Keys.CONTROL, 'a')
        self.xpathS('el-input__inner')[0].send_keys(Keys.BACKSPACE)
        self.xpathS('el-input__inner')[1].send_keys(Keys.CONTROL, 'a')
        self.xpathS('el-input__inner')[1].send_keys(Keys.BACKSPACE)

    def loginButton(self):
        """登录按钮"""
        self.xpath('btn-login').click()
        time.sleep(2)
        asserts = self.xpathS('el-notification__content')[0].text
        time.sleep(2)
        return asserts


    def loginMsg(self, url, account, password):
        """登录信息的参数"""
        self._login(url)
        self._clearInput()
        self.xpathS('el-input__inner')[0].send_keys(account)
        self.xpathS('el-input__inner')[1].send_keys(password)

    def asserts(self, parameter):
        """断言参数"""
        self.xpath('btn-login').click()
        time.sleep(3)
        self.asserts = self.xpathS(parameter)[0].text
        return self.asserts

    def logo(self, url):
        """请求logo连接"""
        self._login(url)
        urls = self.url + url
        r = requests.get(urls).status_code
        return r

    def forget(self, switch=False):
        """忘记密码"""
        self.xpath('忘记密码', 'text()').click()
        time.sleep(2)
        if switch:
            self.xpath('确定','text()').click()
            time.sleep(2)
        asserts = self.xpathS('el-notification__content')[0].text
        time.sleep(1)
        return asserts