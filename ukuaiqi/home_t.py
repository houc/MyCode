from model.my_unittest import MyUnittest
import unittest

class T(MyUnittest):
    def test_y(self):
        self.driver.get(self.url)

if __name__ == '__main__':
    unittest.main()