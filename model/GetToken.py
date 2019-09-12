from . MyConfig import ConfigParameter
from . SeleniumElement import OperationElement


class BrowserToken(OperationElement):
    """
    该类主要用于获取浏览器中的token值
    """
    def __init__(self, driver):
        OperationElement.__init__(self, driver)
        self.config = ConfigParameter()



