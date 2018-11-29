from model.my_unittest import MyUnittest
import unittest,time

class T888(MyUnittest):
    def test_mmm(self):
        self.driver.get(self.url + '/dashboard#started/list')
        self.assertEqual(1,1)