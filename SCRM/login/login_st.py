from model.MyUnitTest import UnitTests,setUpModule,tearDownModule
from SCRM.login.public import ElementsParameter
import unittest


class LoginTestIn(UnitTests):
    def test_accountError(self):
        """错误的用户账户"""
        elements = ElementsParameter(self.driver,self.url)
        elements.login_elements(self.data[1]['account'],self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountLong(self):
        """账号为240位数字"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'] * 5, self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountEnglish(self):
        """账号为英文字符"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'], self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountEnglishLong(self):
        """账号为英文240字符"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'] * 5, self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountAndEnglish(self):
        """账号为英文字符与数字组合"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'], self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountAndEnglishLong(self):
        """账号为英文字符与数字组合110字符"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'] * 5, self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountBoundary(self):
        """账号边界测试"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'], self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountStr(self):
        """账号为字符串"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'], self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    @unittest.skip('暂时测试，跳过一下吧！')
    def test_accountMerge(self):
        """账号为字符串，英文，数字，空格"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'], self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])

    def test_accountSpace(self):
        """账号为空格"""
        elements = ElementsParameter(self.driver, self.url)
        elements.login_elements(self.data[1]['account'], self.data[1]['password'],self.data[2])
        self.result = elements.xpathS('mu-text-field-help')[0].text
        self.assertEqual(self.result, self.data[0])


if __name__ == '__main__':
    unittest.main()