import unittest
from config_path.path_file import get_chrome_driver_path
from selenium import webdriver

class MyUnittest(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        path = get_chrome_driver_path()
        cls.driver = webdriver.Chrome(path)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.url = 'https://ukuaiqi.com'
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()