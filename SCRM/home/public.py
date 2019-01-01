from SCRM.public_transmit import DriverTransmit
from selenium.webdriver.common.keys import Keys

class ElementsParameter(DriverTransmit):
    def home_search(self,url):
        self.driver.get(self.url + url)
        self.xpathS('opt_li_global search')[0].click()

    def help_center(self,url):
        self.driver.get(self.url + url)
        self.xpathS('opt_li_help center')[0].click()
