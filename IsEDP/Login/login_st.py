import unittest

from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from IsEDP.ModuleElement import LoginModules
from IsEDP.Login.public import ACCOUNT, PASSWORD
from IsEDP.Login.public import InterfaceTest


class LoginTest(UnitTests):
    def test_accountError(self):
        """错误的用户名"""
        try:
            self.level = 'P1'
            account = 'admin_admin'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_accountLong(self):
        """用户名长度120字节"""
        try:
            self.level = 'P1'
            account = 'admin_admin' * 12
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_accountSpace(self):
        """用户名为空格"""
        try:
            self.level = 'P1'
            account = ' '
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'loginName cannot be empty'
        except Exception as exc:
            self.error = str(exc)

    def test_accountNull(self):
        """用户名为空"""
        try:
            self.level = 'P1'
            account = ''
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.asserts('el-form-item__error')
            self.second = '请输入用户名'
        except Exception as exc:
            self.error = str(exc)

    def test_accountSymbol(self):
        """用户名为特殊符号"""
        try:
            self.level = 'P1'
            account = '~！@#￥%……&*（）——+'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_accountBoundaryAfter(self):
        """账号边界测试（后）"""
        try:
            self.level = 'P1'
            account = 'admi'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_accountBoundaryFront(self):
        """账号边界测试（前）"""
        try:
            self.level = 'P1'
            account = 'dmin'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_passwordBoundaryAfter(self):
        """密码边界测试（后）"""
        try:
            self.level = 'P1'
            password = '00000'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordBoundaryFront(self):
        """密码边界测试（前）"""
        try:
            self.level = 'P1'
            password = '00000'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordSpace(self):
        """密码为空格"""
        try:
            self.level = 'P1'
            password = ' '
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.loginButton()
            self.second = 'password cannot be empty'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordNull(self):
        """密码为空"""
        try:
            self.level = 'P1'
            password = ''
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.asserts('el-form-item__error')
            self.second = '请输入密码'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordError(self):
        """错误的密码"""
        try:
            self.level = 'P1'
            password = '00000aa'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordLong(self):
        """密码字符120字节"""
        try:
            self.level = 'P1'
            password = '000000' * 20
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_loginLogo(self):
        """检查登录界面logo是否存在"""
        try:
            self.level = 'P3'
            self.urls = '/static/images/logo.bae1317.png'
            elements = LoginModules(self.driver, self.url)
            self.first = elements.logo(self.urls)
            self.second = 200
        except Exception as exc:
            self.error = str(exc)

    def test_passwordForgetNull(self):
        """忘记密码(空账号)"""
        try:
            self.level = 'P1'
            account = ''
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.forget()
            self.second = '请输入账号再点击忘记密码！'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordForgetError(self):
        """忘记密码(错误账号)"""
        try:
            self.level = 'P1'
            account = '080808admin'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.forget(True)
            self.second = 'user {0!r} does not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_passwordSuccessAccount(self):
        """忘记密码（正确账号）"""
        try:
            self.level = 'P1'
            account = 'TESTS'
            password = ''
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, password)
            self.first = elements.forget(True)
            self.second = '新密码已发送到您的手机！'
        except Exception as exc:
            self.error = str(exc)

    def test_errorPhone(self):
        """忘记密码（错误的手机号）"""
        try:
            self.level = 'P1'
            account = 'TESTS'
            password = ''
            modify = InterfaceTest()
            modify.modify_error()
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, password)
            self.first = elements.forget(True)
            self.second = '手机号格式错误'
            modify.modify_correct()
        except Exception as exc:
            self.error = str(exc)

if __name__ == '__main__':
    unittest.main()