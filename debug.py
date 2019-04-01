import unittest


class My(unittest.TestCase):
    def test_ont(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)


dicts = {"ff": "python", "chrome": "selenium", "ie": "unittest"}

for a, b in dicts.items():
    if 'ie' == a:
        print(b)