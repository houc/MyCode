from SCRM.public_transmit import DriverTransmit
from selenium.webdriver.common.keys import Keys

class ElementsParameter(DriverTransmit):
    def login_elements(self,account,password,url):
        self.driver.get(self.url + url)
        self.cssS('mu-text-field-input')[0].send_keys(Keys.CONTROL,'a')
        self.cssS('mu-text-field-input')[0].send_keys(Keys.BACKSPACE)
        self.xpathS('password', '@type')[0].send_keys(Keys.CONTROL,'a')
        self.xpathS('password', '@type')[0].send_keys(Keys.BACKSPACE)
        self.cssS('mu-text-field-input')[0].send_keys(account)
        self.xpathS('password', '@type')[0].send_keys(password)
        self.xpathS('enabled')[0].click()

