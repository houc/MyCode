import unittest

from model.MyUnitTest import setUpModule,tearDownModule,UnitTests
from IsEDP.ModuleElement import LoginModules


class LoginTest(UnitTests):
    def test_accountError(self):
        """错误的用户名"""
        self.level = 'P1'
        account = 'admin_admin'
        password = '000000'
        elements = LoginModules(self.driver,self.url)
        elements.loginMsg(self.urls,account,password)
        elements.loginButton()
        self.first = elements.asserts
        self.second = 'user {} not exist'.format(account)
        self.assertEqual(self.first, self.second)

    def test_accountLong(self):
        """用户名长度120字节"""
        self.level = 'P1'
        account = 'admin_admin' * 12
        password = '000000'
        elements = LoginModules(self.driver,self.url)
        elements.loginMsg(self.urls,account,password)
        elements.loginButton()
        self.first = elements.asserts
        self.second = 'user {} not exist'.format(account)
        self.assertEqual(self.first, self.second)


if __name__ == '__main__':
    unittest.main()