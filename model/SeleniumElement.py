import time
import pykeyboard
import pymouse

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as hover
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.DriverParameter import browser
from model.Yaml import MyConfig
from PIL import ImageGrab


class OperationElement(object):
    """
        浏览器操作封装类
    """

    def __init__(self, driver, timeout=5, detection=0.2, exception=EC.NoSuchElementException):
        """
        初始化类参数
        :param driver: 浏览器session
        :param timeout: 等待超时默认20秒
        :param detection: 默认间隔0.5秒侦查一次元素是否存在或者消失
        :param exception: 默认异常为未能找到元素异常类
        """
        self.driver = driver
        self.key = pykeyboard.PyKeyboard()
        self.mouse = pymouse.PyMouse()
        self.support = WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=detection,
                                     ignored_exceptions=exception)

    def f5(self):
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
        element_source = self.operation_element(source)
        element_target = self.operation_element(target)
        hover(self.driver).drag_and_drop(element_source, element_target).perform()

    def driver_quit(self):
        """
        浏览器退出
        :return:
        """
        self.driver.quit()

    @staticmethod
    def open_browser():
        """
        打开浏览器
        :return: 返回新浏览器的session
        """
        headless = MyConfig('browser').config
        return browser(switch=headless)

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
        elif by == "css selector":
            return self.driver.find_element(By.CSS_SELECTOR, element_value)

    @staticmethod
    def full_windows_screen(path: str, length=None, height=None):
        """
        自定义当前屏幕截图范围
        :param path: 存放截图的路径位置，如：D:\work_file\auto_script\TestUi\config\TestCase.png
        :param length: 自定义截取屏幕长度位置, 默认为当前屏幕的值
        :param height: 自定义截取屏幕宽度位置， 默认为当前屏幕的值
        :return: ...
        """
        screen = ImageGrab.grab()
        if length is not None and height is not None:
            screen.size = length, height
        screen.save(path)

    def screen_base64_shot(self):
        """
        截图
        :return: base64
        """
        return self.driver.get_screenshot_as_base64()

    def execute_js(self, js: str):
        """
        执行js
        :param js: 如:打开新窗口：'window.open("https://www.sogou.com")'
        :return:
        """
        return self.driver.execute_script(js)

    def current_window(self):
        """
        当前窗口句柄
        :return: 返回当前窗口句柄ID
        """
        return self.driver.current_window_handle

    def hovers(self, element):
        """
        悬浮元素
        :param element: self.hovers(((By.XPATH, "(//tr[starts-with(@class, 'ivu-table-row')])[1]")))
        :return: 返回对应的操作元素
        """
        hover_element = self.operation_element(element)
        hover(self.driver).move_to_element(hover_element).perform()

    def more_window(self):
        """
        全部窗口句柄
        :return: 返回全部窗口句柄ID
        """
        return self.driver.window_handles

    def switch_window(self, indexes: int):
        """
        切换窗口
        :param name: 切换到窗口列表名字，如[1]
        :return: 对应的窗口
        """
        windows = self.more_window()
        return self.driver.switch_to.window(windows[indexes])

    def switch_frame(self, frame_reference: str):
        """
        切换frame位置
        :param frame_reference: 框架位置
        :return: 返回对应框架中
        """
        return self.driver.switch_to.frame(frame_reference)

    def release_frame(self):
        """释放frame"""
        return self.driver.switch_to.default_content()

    def close_current_window(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()
    
    def operation_element(self, element):
        """
        显示等待某一个元素是否存在，默认超时20秒，每次0.5秒侦查一次是否存在
        :param element: 如：如：operation_element(By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")).click()
        :param timeout: 如：20
        :param wait_time: 默认等待2秒
        :return: 存在则返回，不存在则抛出异常！
        """
        return self.support.until(EC.presence_of_element_located(element),
                                  message=f'元素: {element}  超时...')

    def is_click(self, element):
        """
        判断元素是否可点击,当第一次点击报错，等待默认时间2秒后再执行点击操作是否可点击，如过还是不可点击，就抛出异常错误
        :param element: self.is_click((By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[5]"))
        :param wait_time: 等待时间
        :return: ....
        """
        is_click = self.support.until(EC.element_to_be_clickable(element),
                                      message=f'元素: {element}  超时...')
        if is_click:
            is_click.click()

    def script_upload(self, path: str):
        """
        使用PyUserInput库上传附件 | 使用该方法时，请勿操作其他程序，否则可能会存在上传失败！
        :param path: 上传文件的对应路径
        :return: ....
        """
        time.sleep(1)
        self.key.tap_key(self.key.shift_key)
        self.key.type_string(path.replace('/', '\\'))
        time.sleep(1)
        self.key.tap_key(self.key.enter_key)

    def script_click(self, x: int, y: int, button: int=1, n: int=1):
        """
        使用PyUserInput库鼠标点击
        :param x: 坐标x
        :param y: 坐标y
        :param button: 按照位置
        :param n: 执行循环次数
        :return: ....
        """
        self.mouse.click(x, y, button, n)

    def method_driver(self, method):
        """
        方法继承
        :param method: 方法
        :return: ...
        """
        return method(self.driver)

    def is_send(self, element, value):
        """
        判断是否可执行输入，当第一次出现异常，默认等待2秒后再次尝试是否可输入，直到再次获得信息
        :param element: self.is_send(By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[5]"), "小明")
        :param value: "小明"
        :param wait_time: 等待时间
        :return: ...
        """
        self.operation_element(element).send_keys(value)

    def is_text(self, element):
        """
        获取元素中的文本值，第一次获取文本值如果为空，就默认等待2秒时间，再次获取
        :param element: self.is_text((By.XPATH, "(//button[starts-with(@class, 'ivu-btn')])[5]"))
        :param wait_time: 等待时间
        :return: 返回对应的文本值
        """
        return self.operation_element(element).text

    def is_attribute(self, element, text, value):
        """
        获取元素列表中的属性值(该项为class)
        :param element: is_attribute((By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"))
        :param text: 属性内容是否包含，包含返回True, 反之返回False
        :param attribute: class
        :return: 返回对应bool，存在返回True，反之False
        """
        attribute_element = self.operation_element(element)
        return text in attribute_element.get_attribute(value)

    def get_attributed(self, element, value):
        """
        获取元素列表中的属性值(该项为class)
        :param element: 元素
        :return: 返回对应的class属性值
        """
        attribute_element = self.operation_element(element)
        return attribute_element.get_attribute(value)

    def is_element(self, element):
        """
        检查元素是否存在
        :param element: is_element((By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"))
        :return: 存在返回True，不存在返回False
        """
        try:
            self.operation_element(element)
            return True
        except TimeoutError:
            return False

    @staticmethod
    def str_conversion(element, *args):
        """
        将元素定义变量中包含$进行参数化转化传递
        :param element: 如，(By.XPATH, "//li[contains(text(),'$')]")
        :param args：将$变更为value
        :return:
        """
        if "$" in element[1]:
            now_value = element[1].replace("$", "{}")
            new_element = (element[0], now_value.format(*args))
            return new_element
        else:
            raise ValueError('无需参数化，请不要调用该方法，或者参数化需要“$”')

    def is_in_text(self, element, content: str):
        """
        断定element的文本值，是否与content的文本值包含，包含返回True， 反之返回False
        :param element: is_text(By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")， "小明")
        :param content:  "小明"
        :return: 相同返回True， 不相同返回False
        """
        return self.support.until(EC.text_to_be_present_in_element(element, content),
                                  message=f'元素: {element}  超时...')

    def is_url_equal(self, url: str):
        """
        断定current_url值，是否与url相对等
        :param url: "http://www.sina.com.cn"
        :return: 相等返回True,不相等返回False
        """
        try:
            is_url = self.support.until(EC.url_to_be(url), message=f'url: {url} 超时...')
        except TimeoutError:
            return False
        else:
            return is_url

    def get_url(self):
        """
        获取当前url
        :return: 返回获取的url
        """
        url = _Get()
        return self.support.until(url, message=f'url: {url} 超时...')

    def is_url_contain(self, url: str):
        """
        断定current_url值，是否包含url值
        :param url: "http://www.sina"
        :return: 包含返回True,不包含返回False
        """
        try:
            is_url = self.support.until(EC.url_contains(url), message=f'url: {url} 超时...')
        except TimeoutError:
            return False
        else:
            return is_url

    def is_attribute_value(self, element, text: str):
        """
        断定当前element下value属性值，是否包含text
        :param element: is_attribute(By.XPATH, "//*[contains(text(),'请选择要登录的公司')]")， "小明")
        :param text: "true"
        :return: 包含返回True,不相等返回False
        """
        return self.support.until(EC.text_to_be_present_in_element_value(element, text),
                                  message=f'元素: {element}  超时...')

    def is_displayed(self, element):
        """
        检查元素是否可以在web界面上看见
        :param element: 如，self.is_element_exist((By.XPATH, "//*[contains(text(),'请选择要登录的公司')]"))
        :return: 可见返回True，反之返回False
        """
        return self.support.until(EC.visibility_of_element_located(element),
                                  message=f'元素: {element}  超时...')


class _Get(object):
    """获取当前页面url"""
    def __call__(self, driver):
        return driver.current_url

