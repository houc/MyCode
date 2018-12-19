import time

from IsEDP.Elements import DriverTransmit


class LoginModule(DriverTransmit):
    def success_login(self,account,password):
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
    def _menu(self,url):
        """菜单的公共方法"""
        self.driver.get(self.url + url)

    def CreateMenuNull(self,url):
        """创建菜单名称为空"""
        self._menu(url)
        self.xpathS('新增', 'text()')[0].click()
        self.xpathS('确认', 'text()')[1].click()
        time.sleep(2)
        self.asserts = self.xpathS('el-notification__content')[0].text


class LoginModules(DriverTransmit):
    def _login(self,url):
        """登录公共方法"""
        self.driver.get(self.url + url)

    def _clearInput(self):
        """清除用户名和密码中的内容"""
        self.xpathS('el-input__inner')[0].clear()
        self.xpathS('el-input__inner')[1].clear()

    def loginButton(self):
        """登录按钮"""
        self.xpath('btn-login').click()
        time.sleep(2)
        self.asserts = self.xpathS('el-notification__content')[0].text

    def loginMsg(self,url,account,password):
        """登录信息的参数"""
        self._login(url)
        self._clearInput()
        self.xpathS('el-input__inner')[0].send_keys(account)
        self.xpathS('el-input__inner')[1].send_keys(password)