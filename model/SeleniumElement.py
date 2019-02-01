from selenium.webdriver.common.by import By


class _OperationElement(object):
    """
        浏览器操作封装类
    """

    def __init__(self, driver):
        self.driver = driver

    def F5(self):
        """浏览器刷新"""
        self.driver.refresh()

    def get(self, url: str):
        """请求url的参数"""
        self.driver.get(url)


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
            ElementLocation(self.driver).XPATH(手机号/邮箱*/../input!!send")
        """
        step = element.split('!!')[1]
        path_name = element.split('!!')[0]
        if step == "text":
            if '@' in path_name.split('*')[0]:
                text = element.split('@')[0]
                path = element.split('@')[1].split('*')[1].split('!!')[0]
                if '$' in path_name.split('*')[0]:
                    first_path = element.split('$')[0]
                    return self.driver.find_element(By.XPATH, '//{}[text()="{}"]{}'.format(first_path, text, path)).text
                else:
                    return self.driver.find_element(By.XPATH, '//*[text()="{}"]{}'.format(text, path)).text
            else:
                text = element.split('*')[0]
                path = element.split('*')[1].split('!!')[0]
                if '$' in path_name.split('*')[0]:
                    first_path = element.split('$')[0]
                    return self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                                    format(first_path, text, path)).text
                else:
                    return self.driver.find_element(By.XPATH, '//*[contains(text(), "{}")]{}'.format(text, path)).text
        elif step == "send":
            if '@' in path_name.split('*')[0]:
                text = element.split('@')[0]
                path = element.split('@')[1].split('*')[1].split('!!')[0]
                if '$' in path_name.split('*')[0]:
                    first_path = element.split('$')[0]
                    self.driver.find_element(By.XPATH, '//{}[text()="{}"]{}'.format(first_path, text, path)).\
                        send_keys(param)
                else:
                    self.driver.find_element(By.XPATH, '//*[text()="{}"]{}'.format(text, path)).send_keys(param)
            else:
                text = element.split('*')[0]
                path = element.split('*')[1].split('!!')[0]
                if '$' in path_name.split('*')[0]:
                    first_path = element.split('$')[0]
                    self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                             format(first_path, text, path)).send_keys(param)
                else:
                    self.driver.find_element(By.XPATH, '//*[contains(text(), "{}")]{}'.
                                             format(text, path)).send_keys(param)
        elif step == "click":
            if '@' in path_name.split('*')[0]:
                text = element.split('@')[0]
                path = element.split('@')[1].split('*')[1].split('!!')[0]
                if '$' in path_name.split('*')[0]:
                    first_path = element.split('$')[0]
                    self.driver.find_element(By.XPATH, '//{}[text()="{}"]{}'.format(first_path, text, path)).\
                        send_keys(param)
                else:
                    self.driver.find_element(By.XPATH, '//*[text()="{}"]{}'.format(text, path)).send_keys(param)
            else:
                text = element.split('*')[0]
                path = element.split('*')[1].split('!!')[0]
                if '$' in path_name.split('*')[0]:
                    first_path = element.split('$')[0]
                    self.driver.find_element(By.XPATH, '//{}[contains(text(), "{}")]{}'.
                                             format(first_path, text, path)).click()
                else:
                    self.driver.find_element(By.XPATH, '//*[contains(text(), "{}")]{}'.
                                             format(text, path)).click()

    def CSS(self, element: str, send=""):
        """
        结合selenium，封装一个CSS
        :param element: "input[name='wd']", "input[name]".....
        :param param: send_keys里面的参数
        :return: 对应元素值
        """
        elements = element.split("!!")[0]
        type_event = element.split('!!')[1]
        if type_event == "click":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).click()
        elif type_event == "send":
            self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).send_keys(send)
        elif type_event == "text":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).text
            return value
        elif type_event == "display":
            value = self.driver.find_element(By.CSS_SELECTOR, '{}'.format(elements)).is_displayed()
            return value



if __name__ == '__main__':
    text = 'span$登录&*/../../..!!click'
    print(text.split('$')[0])