import unittest
import time
import os

from config_path.path_file import PATH
from model.MyUnitTest import setUpModule, tearDownModule, UnitTests
from model.SkipModule import Skip, current_module
from SCRM.marketing_transformation.currency import MarketingTransformationElement

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class TestMarketingTransformation(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    """
    RE_LOGIN = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.dirname(__file__).split("\\")[-1]
    
    def test_mailCopy(self):
        """
        进入邮件营销库，复制第一条营销邮件:

        1、通过url访问邮箱邮件库;

        2、hover后点击复制;
        """
        try:
            driver = MarketingTransformationElement(self.driver)
            driver.get(self.url)
            driver.test_element(location=1)
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = driver.assert_url()  # 此项为必填，第一个断言值
        except Exception as exc:
            self.error = str(exc)

    def test_up(self):
        """
        进入邮件营销库，复制第一条营销邮件:

        1、通过url访问邮箱邮件库;

        2、hover后点击复制;

        3、验证是否能正常跳转到复制页面
        """
        try:
            driver = MarketingTransformationElement(self.driver)
            driver.get(self.url)
            driver.ups()
            
            time.sleep(2)
            driver.screen_shot(self.screenshots_path)
            self.first = ""  # 此项为必填，第一个断言值
        except Exception as exc:
            self.error = str(exc)

