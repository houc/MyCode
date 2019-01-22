import json

from model.MyConfig import ConfigParameter
from model.PrintColor import RED_BIG


class BrowserToken(object):
    """
    该类主要用于获取浏览器中的token值
    """
    def __init__(self, driver):
        self.driver = driver
        self.write_ini = ConfigParameter().write_ini

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
            self.write_ini(child="Authorization", content=conversion_token)
        else:
            print(RED_BIG, "TOKEN未能在浏览器中获取成功，TOKEN写入失败")

