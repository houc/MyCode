from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as hover
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.DriverParameter import browser
from model.Yaml import MyYaml
from model.PrintColor import RED_BIG


class OperationElement(object):
    """
        浏览器操作封装类
    """

    def __init__(self, driver, timeout=20, detection=1, exception=EC.NoSuchElementException):
        """
        初始化类参数
        :param driver: 浏览器session
        :param timeout: 等待超时默认20秒
        :param detection: 默认间隔0.2秒侦查一次元素是否存在或者消失
        :param exception: 默认异常为未能找到元素异常类
        """
        self.driver = driver
        self.support = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=detection,
                                     ignored_exceptions=exception)

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
        hover(self.driver).drag_and_drop(self.operation_element(source), self.operation_element(target)).perform()

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

    def _find_element(self, element):
        """
        操作类元素
        :param element: 如：（By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"）
        :return: 对应的元素
        """
        by = element[0]
        element_value = element[1]
        if by == "xpath":
            return self.driver.find_element(By.XPATH, element_value)
        elif by == "css":
            return self.driver.find_element(By.CSS_SELECTOR, element_value)

    def screen_shot(self, path):
        """
        截图
        :param path: 存放截图的路径位置，如：D:\work_file\auto_script\TestUi\config\TestCase.png
        :return: None
        """
        self.driver.save_screenshot(path)

    def execute_js(self, js):
        """
        执行js
        :param js: 如:打开新窗口：'window.open("https://www.sogou.com")'
        :return:
        """
        return self.driver.execute_script(js)

    def current_windows(self):
        """
        当前窗口句柄
        :return: 返回当前窗口句柄ID
        """
        return self.driver.current_window_handle

    def more_windows(self):
        """
        全部窗口句柄
        :return: 返回全部窗口句柄ID
        """
        return self.driver.window_handles

    def switch_windows(self, name: int):
        """
        切换窗口
        :param name: 切换到窗口列表名字，如[1]
        :return:
        """
        windows = self.more_windows()
        return self.driver.switch_to_window(windows[name])
    
    def operation_element(self, element):
        """
        显示等待某一个元素是否存在，默认超时20秒，每次0.5秒侦查一次是否存在
        :param element: 如：如：operation_element(By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")).click()
        :param timeout: 如：20
        :return: 存在则返回，不存在则抛出异常！
        """
        global exist_element
        try:
            exist_element = self.support.until(EC.presence_of_element_located(element))
        except Exception as exc:
            print(RED_BIG, exc, element, "超时或者不存在...\n")
            return False
        else:
            return exist_element

    def is_click(self, element, wait_time=2):
        """
        判断元素是否可点击,当第一次点击报错，等待默认时间2秒后再执行点击操作是否可点击，如过还是不可点击，就抛出异常错误
        :param element: self.is_click((By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[5]"))
        :param wait_time: 等待时间
        :return:
        """
        try:
            self.operation_element(element).click()
        except Exception:
            import time
            time.sleep(wait_time)
            self.operation_element(element).click()

    def is_text(self, element, wait_time=2):
        """
        获取元素中的文本值，第一次获取文本值如果为空，就默认等待2秒时间，再次获取
        :param element: self.is_text((By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[5]"))
        :param wait_time: 等待时间
        :return: 返回对应的文本值
        """
        value = self.operation_element(element).text
        if not value:
            import time
            time.sleep(wait_time)
            value = self.operation_element(element).text
        return value

    def is_attribute_class(self, element, text):
        """
        获取元素列表中的属性值(该项为class)
        :param element: is_attribute((By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"))
        :param text: 属性内容是否包含，包含返回True, 反之返回False
        :param attribute: class
        :return: 返回对应bool，存在返回True，反之False
        """
        attribute_value = self.operation_element(element).get_attribute('class')
        return text in attribute_value

    def is_element(self, element):
        """
        检查元素是否存在
        :param element: is_element((By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"))
        :return: 存在返回True，不存在返回False
        """
        try:
            self._find_element(element)
            return True
        except EC.NoSuchElementException:
            return False

    def str_conversion(self, element, value):
        """
        将元素定义变量中包含$进行参数化转化传递
        :param element: 如，(By.XPATH, "//li[contains(text(),'$')]")
        :param value：将$变更为value
        :return:
        """
        if "$" in element[1]:
            now_value = element[1].replace("$", "{}")
            return (element[0], now_value.format(value))

    def is_in_text(self, element, content: str):
        """
        断定element的文本值，是否与content的文本值包含，包含返回True， 反之返回False
        :param element: is_text(By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")， "小明")
        :param content:  "小明"
        :return: 相同返回True， 不相同返回False
        """
        return self.support.until(EC.text_to_be_present_in_element(element, content))

    def is_url_equal(self, url: str):
        """
        断定current_url值，是否与url相对等
        :param url: "http://www.sina.com.cn"
        :return: 相等返回True,不相等返回False
        """
        return self.support.until(EC.url_to_be(url))

    def is_url_contain(self, url: str):
        """
        断定current_url值，是否包含url值
        :param url: "http://www.sina"
        :return: 包含返回True,不包含返回False
        """
        return self.support.until(EC.url_contains(url))

    def is_attribute_value(self, element, text: str):
        """
        断定当前element下value属性值，是否包含text
        :param element: is_attribute(By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")， "小明")
        :param text: "true"
        :return: 包含返回True,不相等返回False
        """
        return self.support.until(EC.text_to_be_present_in_element_value(element, text))

    def is_displayed(self, element):
        """
        检查元素是否可以在web界面上看见
        :param element: 如，self.is_element_exist((By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"))
        :return: 可见返回True，反之返回False
        """
        return self.support.until(EC.visibility_of_element_located(element))


