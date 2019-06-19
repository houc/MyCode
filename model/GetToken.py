import json

from model.MyConfig import ConfigParameter
from model.PrintColor import RED_BIG
from model.SeleniumElement import OperationElement


class BrowserToken(OperationElement):
    """
    该类主要用于获取浏览器中的token值
    """
    def __init__(self, driver):
        OperationElement.__init__(self, driver)
        self.config = ConfigParameter()

    def get_token(self):
        """
        通过driver获取到driver中的token
        """
        js = "return window.localStorage.getItem('token')"
        token = self.driver.execute_script(js)
        self._write_token(token)

    def _write_token(self, token: str):
        """处理token样式后并将token写入到config.ini中"""
        if token is not None:
            conversion_token = json.loads(token)["val"]
            self.config.write_ini(content=conversion_token)
        else:
            print(RED_BIG, "TOKEN未能在浏览器中获取成功，TOKEN写入失败")


