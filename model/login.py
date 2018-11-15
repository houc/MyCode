from model.my_unittest import MyUnittest
import unittest


class login(MyUnittest):
    def test_login_success(self):
        """登录成功"""
        url = self.url + '/login'
        self.driver.get(url)

if __name__ == '__main__':
    unittest.main()