import unittest
import os

from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from IsEDP.ModuleElement import LoginModules
from IsEDP.Login.currency import ACCOUNT, PASSWORD, InterfaceTest

_PATH = os.path.realpath(__file__)
_SKIP = Skip(current_module(_PATH)).is_skip


@unittest.skipIf(_SKIP, '登录认证更换，登录用例暂时弃用')
class LoginTest(UnitTests):
    def test_accountError(self):
        """
        错误的用户名:
        1、输入错误的用户名
        """
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
        """
        用户名长度120字节:
        1、输入用户名长度120字节
        """
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
        """
        用户名为空格:
        1、输入正确的登录用户名密码；
        2、登录用户名为空格
        """
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
        """
        用户名为空:
        1、输入正确的登录用户名密码；
        2、登录用户名为空
        """
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
        """
        用户名为特殊符号:
        1、输入正确的登录用户名密码；
        2、登录用户名为特殊字符
        """
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
        """
        账号边界测试:
        1、正确的登录用户名的密码；
        2、输入的正确登录用户名删除后面第一位数
        """
        try:
            self.level = 'P1'
            account = ACCOUNT[:-1]
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_accountBoundaryFront(self):
        """
        账号边界测试:
        1、正确的登录用户名的密码；
        2、输入的正确登录用户名删除前面第一位数
        """
        try:
            self.level = 'P1'
            account = ACCOUNT[1:]
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, PASSWORD)
            self.first = elements.loginButton()
            self.second = 'user {} not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)

    def test_passwordBoundaryAfter(self):
        """
        密码边界测试:
        1、正确的登录用户名；
        2、输入的正确密码删除前面第一位数
        """
        try:
            self.level = 'P1'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, PASSWORD[:-1])
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordBoundaryFront(self):
        """
        密码边界测试:
        1、正确的登录用户名；
        2、输入的正确密码删除前面第一位数
        """
        try:
            self.level = 'P1'
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, PASSWORD[1:])
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_passwordSpace(self):
        """
        密码为空格:
        1、输入正确的用户名；
        2、输入的密码为空格
        """
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
        """
        密码为空:
        1、输入正确的用户名；
        2、不输入密码
        """
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
        """
        错误的密码:
        1、正确的用户名；
        2、输入的密码错误
        """
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
        """
        密码:
        1、正确的登录用户名；
        2、密码长度字符在120个字节
        """
        try:
            self.level = 'P2'
            password = '000000' * 20
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, ACCOUNT, password)
            self.first = elements.loginButton()
            self.second = 'password error'
        except Exception as exc:
            self.error = str(exc)

    def test_loginLogo(self):
        """
        检查登录界面logo是否存在:
        1、获取到logo的url进行请求并断言
        """
        try:
            self.level = 'P3'
            self.urls = '/static/images/logo.bae1317.png'
            elements = LoginModules(self.driver, self.url)
            self.first = elements.logo(self.urls)
            self.second = 200
        except Exception as exc:
            self.error = str(exc)

    def test_passwordForgetNull(self):
        """
        忘记密码:
        1、未输入登录用户名
        """
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
        """
        忘记密码:
        1、错误的登录用户名，即在系统中不存在的登录用户名
        """
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
        """
        忘记密码:
        1、登录用户名的手机号码正确
        """
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
        """
        忘记密码:
        1、通过UI输入用户名；
        2、通过接口将输入的用户名的手机号变更为错误的手机号码（10位数）；
        3、在通过UI找回密码
        """
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

    def test_asynchronousOperation(self):
        """
        异步操作:
        1、先用UI将正确的账号密码输入到对应的输入框中，在通过接口将正确的账号删除掉；
        2、在用UI执行登录
        """
        try:
            self.level = 'P1'
            account = 'TESTS'
            password = ''
            modify = InterfaceTest()
            elements = LoginModules(self.driver, self.url)
            elements.loginMsg(self.urls, account, password)
            modify.del_user()
            self.first = elements.forget(True)
            self.second = 'user {0!r} does not exist'.format(account)
        except Exception as exc:
            self.error = str(exc)


if __name__ == '__main__':
    unittest.main()
