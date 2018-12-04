from model.my_unittest import *

class H(MyUnittest):
    def test(self):
        self.log = 'test'
        self.driver.get(self.url + '/dashboard#perform/list')
        self.assertEqual(1,6)

    def test_test1(self):
        self.log = 'test_test1'
        self.driver.get(self.url + '/dashboard#organization/list')
        self.assertEqual(4,4)

if __name__ == '__main__':
    unittest.main()