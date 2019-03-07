from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from model.DriverParameter import browser
from model.Yaml import MyYaml


class _OperationElement(object):
    """
        浏览器操作封装类
    """

    def __init__(self, driver):
        """初始化"""
        self.driver = driver

    def F5(self):
        """浏览器刷新"""
        self.driver.refresh()

    def get(self, url: str):
        """请求url的参数"""
        self.driver.get(url)

    def drag(self, source, target):
        """
        元素拖拽
        :param source: 拖拽元素对象
        :param target: 拖拽元素位置
        """
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def driver_quit(self):
        """
        浏览器退出
        :return:
        """
        self.driver.quit()

    def open_browser(self):
        """
        打开浏览器
        :return: 返回新浏览器的session
        """
        return browser(MyYaml('browser').config)

    def is_element_exist(self, by, element):
        """
        检查元素是否存在
        :param element: 元素, 如：//*[text()='密码错误请重新输入']/..
        :param by: 指定的方法，如：By.XPATH
        :return: 存在返回True，反之返回False
        """
        try:
            self.driver.find_element(by, element)
            return True
        except:
            return False

class ElementLocation(_OperationElement):
    """
        浏览器元素定位封装类
    """

    def __init__(self, driver):
        super(ElementLocation, self).__init__(driver)

    def find_element(self, by):
        """
        元素处理
        :param by:
        :return:
        """



if __name__ == '__main__':
    text = "//*[text()='账号未注册']/..!!text"
    print(text.split("!!")[1])