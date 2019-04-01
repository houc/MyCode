import unittest


class My(unittest.TestCase):
    def test_ont(self):
        self.assertEqual(1, 1)
        self.assertNotEqual(1, 2)