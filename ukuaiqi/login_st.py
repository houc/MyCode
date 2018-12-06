from model.my_unittest import MyUnittest

class case(MyUnittest):
    def test_login(self):
        self.driver.get(self.url + '/login')

        # self.result = ghg
        self.assertEqual(1,3)