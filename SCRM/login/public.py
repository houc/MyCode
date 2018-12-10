from SCRM.public_transmit import DriverTransmit

class ElementsParameter(DriverTransmit):
    def login_elements(self,account,password):
        self.driver.get(self.url + '/#/account/login')
        self.xpathS('mu-text-field-input').clear()
        self.xpathS('password', '@type').clear()
        self.xpathS('mu-text-field-input')[0].send_keys(account)
        self.xpathS('password', '@type')[0].send_keys(password)
        self.xpathS('enabled')[0].click()
