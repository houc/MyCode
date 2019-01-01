from selenium.webdriver.common.by import By


class DriverTransmit(object):
    def __init__(self,driver,url):
        """初始化"""
        self.driver = driver
        self.url = url

    def xpathS(self,parameter,type='@class',tag='*'):
        """xpath多元素定位"""
        return self.driver.find_elements(By.XPATH,'//{}[contains({}, "{}")]'.format(tag,type,parameter))

    def cssS(self,css):
        """css多元素定位"""
        return self.driver.find_elements(By.CSS_SELECTOR,'.{}'.format(css))

    def id(self,id):
        """id定位"""
        return self.driver.find_element(By.ID,'{}'.format(id))

    def success_login(self,account,password):
        """成功登陆"""
        self.driver.get(self.url + '/#/account/login')
        self.xpathS('mu-text-field-input')[0].clear()
        self.xpathS('password', '@type')[0].clear()
        self.xpathS('mu-text-field-input')[0].send_keys(account)
        self.xpathS('password','@type')[0].send_keys(password)
        self.xpathS('enabled')[0].click()
        self.xpathS('ivu-menu-item')[0].click()
        assert self.xpathS('menu-name')[0].text == '我的工作台'

    def opens_if(self):
        """判断网址是否打开"""
        self.driver.get(self.url + '/#/account/login')
        assert self.cssS('ivu-tabs-tab.ivu-tabs-tab-active')[0].text == '账号密码登录'
