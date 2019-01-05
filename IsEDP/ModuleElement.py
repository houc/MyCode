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
        time.sleep(2)
        self.asserts = self.xpathS('el-notification__content')[0].text
        self._close_menu()
        return self.asserts

    def createParentMenuScroll(self, url):
        """创建菜单父级菜单滚动"""
        self._menu(url)
        self.xpathS('新增', 'text()')[0].click()
        self.xpathS('el-input el-input--suffix')[0].click()
        self.element_scroll('el-select-dropdown__item', -1)
        time.sleep(1)
        self.xpathS('el-select-dropdown__item')[-1].click()
        self.xpathS('el-input el-input--suffix')[0].click()
        time.sleep(1)
        self.asserts = self.xpathS('el-select-dropdown__item')[-1].text
        self._close_menu()
        return self.asserts

    def createNullCancel(self, url):
        """创建菜单取消"""
        self._menu(url)
        self.xpathS('新增', 'text()')[0].click()
        self.xpathS('取消', 'text()')[1].click()
        time.sleep(1)
        self.asserts = self.xpathS('el-dialog__wrapper')[2].is_displayed()
        return self.asserts

    def _close_menu(self):
        """关闭新建菜单弹窗"""
        self.xpathS('el-dialog__headerbtn')[2].click()
        time.sleep(1)


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