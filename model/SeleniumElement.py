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
        flag = True
        try:
            self.driver.find_element(by, element)
        except:
            flag = False
        finally:
            return flag


class ElementLocation(_OperationElement):
    """
        浏览器元素定位封装类
    """

    def __init__(self, driver):
        super(ElementLocation, self).__init__(driver)

    def XPATH(self, element: str, param=""):
        """
        结合selenium，封装一个xpath文字元素定位
        Usage:
            ElementLocation(self.driver).XPATH(//*[text()='手机号/邮箱']/../div[1]/input!!click")
        """
        elements = element.split("!!")[0]
        type_event = element.split('!!')[1]
        if type_event == "click":
            self.driver.find_element(By.XPATH, '{}'.format(elements)).click()
        elif type_event == "send":
            self.driver.find_element(By.XPATH, '{}'.format(elements)).send_keys(param)
        elif type_event == "text":
            value = self.driver.find_element(By.XPATH, '{}'.format(elements)).text
            return value
        elif type_event == "display":
            value = self.driver.find_element(By.XPATH, '{}'.format(elements)).is_displayed()
            return value
        elif type_event == 'exist':
            return self.is_element_exist(by=By.XPATH, element=elements)
        else:
            return self.driver.find_element(By.XPATH, '{}'.format(elements))

    def CSS(self, element: str, param=""):
        """
        结合selenium，封装一个CSS

        :param element: "input[name='wd']", "input[name]".....
        :param param: send_keys里面的参数
        :return: 对应元素值
        """
        global dragF
        elements = element.split("!!")[0]
        type_event = element.split('!!')[1]
        if type_event == "click":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).click()
        elif type_event == "send":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).send_keys(param)
        elif type_event == "text":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).text
            return value
        elif type_event == "display":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).is_displayed()
            return value
        elif type_event == 'exist':
            return self.is_element_exist(by=By.CSS_SELECTOR, element=elements)
        else:
            return self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements))
        if type_event == "dragF":
            dragF = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements))
        if type_event == "dragS":
            dragS = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements))
            self.drag(dragF, dragS)

    def element_handle(self, element: list, switch=False):
        """
        处理元素
        :param element: 所有元素：包含xpath、css
        :return: switch为真，则断言，并且返回断言获取的值
        """
        if isinstance(element, list):
            for a in element:
                if "CSS:" in a:
                    value = a.split("CSS:")[1]
                    if '#' in value:
                        re_value = value.split("#")[0]
                        param = value.split("#")[1]
                        if switch:
                            return self.CSS(re_value, param)
                        else:
                            self.CSS(re_value, param)
                    else:
                        if switch:
                            return self.CSS(value)
                        else:
                            self.CSS(value)
                elif "XPATH:" in a:
                    value = a.split("XPATH:")[1]
                    if '#' in value:
                        re_value = value.split("#")[0]
                        param = value.split("#")[1]
                        if switch:
                            return self.XPATH(re_value, param)
                        else:
                            self.XPATH(re_value, param)
                    else:
                        if switch:
                            return self.XPATH(value)
                        else:
                            self.XPATH(value)
        else:
            raise TypeError("element参数不是列表")



if __name__ == '__main__':
    text = "//*[text()='账号未注册']/..!!text"
    print(text.split("!!")[1])