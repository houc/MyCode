import webbrowser
import pykeyboard
import time
import dataclasses

from PIL import ImageGrab
from selenium.webdriver.common.action_chains import ActionChains as Opera
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from . MyException import NoUrlTimeoutError
from . ElementSupport import (GetCurrentUrl, PureClick)
from . MyException import (UntilNoElementOrTimeoutError,
                           UntilNotNotElementOrTimeoutError)


@dataclasses.dataclass
class _VariousElementTypesDisplayWaiting(object):
    """
    该类用于各种元素类型显示等待
    智能定义主要用于操作元素时可自定义，可灵活调用，可复用，可多线程......
    """
    driver: webbrowser
    timeout: float
    detection: float
    exception: EC

    def __post_init__(self):
        self.action = Wait(driver=self.driver, timeout=self.timeout, poll_frequency=self.detection,
                           ignored_exceptions=self.exception)

    def opera_element(self, element):
        """
        操作单个元素，并判断元素在规定的时间内是否出现
        :param element: (By.XPATH, "//div[text()='百度一下']")
        :return: 元素已找到则返回对应元素，反之则抛出异常错误！
        """
        return self.action.until(EC.presence_of_element_located(element),
                                 message=UntilNoElementOrTimeoutError(self.timeout, element))

    def opera_elements(self, elements):
        """
        操作多个元素，并判断元素在规定的时间内是否出现
        :param element: (By.XPATH, "//div[text()='百度一下']")
        :return: 元素已找到则返回对应元素以列表方式返回，反之则抛出异常错误！
        """
        return self.action.until(EC.presence_of_all_elements_located(elements),
                                 message=UntilNoElementOrTimeoutError(self.timeout, elements))

    def opera_element_not(self, element):
        """
        操作单个元素，并判断元素在规定的时间内是否消失
        :param element: (By.XPATH, "//div[text()='百度一下']")
        :return: 元素未找到则返回True，反之则抛出异常错误！
        """
        return self.action.until_not(EC.presence_of_element_located(element),
                                     message=UntilNotNotElementOrTimeoutError(self.timeout, element))

    def opera_elements_not(self, element):
        """
        操作多个元素，并判断元素在规定的时间内是否消失
        :param element: (By.XPATH, "//div[text()='百度一下']")
        :return: 元素未找到则返回True，反之则抛出异常错误！
        """
        return self.action.until_not(EC.presence_of_all_elements_located(element),
                                     message=UntilNotNotElementOrTimeoutError(self.timeout, element))


@dataclasses.dataclass
class _MouseToOperations(_VariousElementTypesDisplayWaiting):
    """
    该类用于鼠标操作一些对应元素
    对应方法中嵌套对应显示等待时间
    """

    def __post_init__(self):
        super(_MouseToOperations, self).__post_init__()
        self.mouse_support = Opera(self.driver)

    def drag_and_drop(self, source, target):
        """
        将单个元素进行拖拽到另一个元素中
        :param source: 执行拖拽的元素
        :param target: 到另一个元素位置
        """
        source_element = self.opera_element(source)
        target_element = self.opera_element(target)
        self.mouse_support.drag_and_drop(source=source_element, target=target_element).perform()

    def drag_and_drop_by_offset(self, element, x_offset: int, y_offset: int):
        """
        单个元素进行拖拽到指定的x坐标和y坐标位置
        :param element: (By.XPATH, "//div[text()='百度一下']")
        :param x_offset: 220
        :param y_offset: 560
        """
        is_element = self.opera_element(element)
        self.mouse_support.drag_and_drop_by_offset(source=is_element, xoffset=x_offset, yoffset=y_offset).perform()

    def hovers(self, element):
        """
        悬浮在元素上
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.move_to_element(to_element=is_element).perform()

    def double_click(self, element):
        """
        鼠标左键双击元素
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.double_click(on_element=is_element).perform()

    def right_click(self, element):
        """
        鼠标右键元素
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.context_click(on_element=is_element).perform()

    def click(self, element):
        """
        左键单击元素, 元素出现并且校验是否可点击
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.click(on_element=is_element).perform()

    def send_keys_to_element(self, element, *keys_to_send):
        """
        通过元素回传内容: 找到元素后，先执行点击操作，在执行回传
        :param element: (By.XPATH, "//div[text()='百度一下']")
        :param keys_to_send: value：卧槽一下！
        """
        is_element = self.opera_element(element)
        self.mouse_support.send_keys_to_element(is_element, *keys_to_send).perform()


@dataclasses.dataclass
class _OtherOperationClass(_MouseToOperations):

    def __post_init__(self):
        super(_OtherOperationClass, self).__post_init__()
        self.keyboard = pykeyboard.PyKeyboard()

    def local_upload_attachments(self, path: str):
        # 本地上传附件
        time.sleep(1)
        self.keyboard.tap_key(self.keyboard.shift_key)
        local_path = path.replace('/', '\\')
        self.keyboard.type_string(local_path)
        time.sleep(1)
        self.keyboard.tap_key(self.keyboard.enter_key)

    @staticmethod
    def parametrization(element, *args):
        # 元素参数转化
        if "$" in element[1]:
            now_value = element[1].replace("$", "{}")
            new_element = (element[0], now_value.format(*args))
            return new_element
        else:
            raise ValueError('No parameter is required. Please do not call this method or parameter it“$”')

    @staticmethod
    def full_window_screen(path: str, length=None, height=None):
        # 截屏当前屏幕（未通过selenium）
        screen = ImageGrab.grab()
        if length is not None and height is not None:
            screen.size = length, height
        screen.save(path)

    def f5(self):
        # 刷新浏览器
        self.driver.refresh()

    def get(self, url: str):
        # 请求需访问的地址
        self.driver.get(url)

    def quit(self):
        # 浏览器退出
        self.driver.quit()

    def screen_base64_shot(self):
        # 截屏浏览器操作屏幕（base64）
        return self.driver.get_screenshot_as_base64()

    def screen_shot(self, path: str):
        # 截屏当前浏览器（jpg、png、jpeg）
        self.driver.save_screenshot(path)

    def execute_js(self, js: str, *args):
        # 使用js操作浏览器
        return self.driver.execute_script(js, *args)

    def current_window(self):
        # 获取浏览器中当前操作窗口的句柄
        return self.driver.current_window_handle

    def more_window(self):
        # 获取浏览器全部操作窗口句柄
        return self.driver.window_handles

    def page_source(self):
        # 获取源码
        return self.driver.page_source

    def switch_window(self, indexes: int):
        # 切换浏览器窗口句柄
        window = self.more_window()
        return self.driver.switch_to.window(window[indexes])

    def release_iframe(self):
        # 回跳至默认dom上
        return self.driver.switch_to.default_content()

    def close_current_window(self):
        # 关闭当前浏览器窗口
        self.driver.close()

    def forward(self):
        # 前进
        self.driver.forward()

    def back(self):
        # 后退
        self.driver.back()

    def get_log(self, log_type):
        # 获取日志信息
        return self.driver.get_log(log_type)

    def get_cookie(self, name):
        # 获取浏览器cookie
        return self.driver.get_cookie(name)

    def method_driver(self, method):
        # 定义driver继承
        return method(self.driver)

    def get_current_url(self):
        # 获取当前url
        url = GetCurrentUrl()
        return self.action.until(url, message=NoUrlTimeoutError(self.timeout))

    def pure_click(self, element):
        # 点击元素，存在直接操作点击
        by = PureClick(element)
        self.action.until(by, message=f'操作点击元素 {element} 超时或不存在...')


class OperationElement(_OtherOperationClass):
    # 浏览器所需元素操作方法封装类

    def __init__(self, driver, timeout=5, detection=0.2, exception=EC.NoSuchElementException):
        super(_OtherOperationClass, self).__init__(driver=driver, timeout=timeout,
                                                   detection=detection, exception=exception)

    def switch_iframe(self, frame_element):
        # 切换到iframe的dom上
        iframe = self.action.until(EC.frame_to_be_available_and_switch_to_it(frame_element),
                                   message=f'iframe_element:  {frame_element}  timeout...')
        if not iframe:
            raise EC.NoSuchFrameException(f'switch {frame_element} it failed！')

    def is_click(self, element):
        # 执行元素可见点击操作
        clicked = self.action.until(EC.element_to_be_clickable(element),
                                    message=f'element: {element}  timeout...')
        if clicked:
            clicked.click()
        else:
            raise EC.NoSuchElementException(f'element: {element}  Not visible or enabled...')

    def send_keys(self, element, *value: str):
        # 元素是否可输入对应内容
        is_element = self.opera_element(element)
        is_element.send_keys(*value)

    def submit(self, element):
        # 元素是否可提交
        is_element = self.opera_element(element)
        is_element.submit()

    def get_text(self, element):
        # 获取在规定的时间内元素中文本值
        is_element = self.opera_element(element)
        return is_element.text

    def get_tag(self, element):
        # 获取元素中tag名称
        is_element = self.opera_element(element)
        return is_element.tag_name

    def is_element(self, element):
        # 判断元素在规定的时间段内是否存在
        try:
            is_element = self.opera_element(element)
            return is_element
        except TimeoutException:
            return False

    def is_elements(self, element):
        # 判断多个元素在规定的时间段内是否存在
        try:
            is_element = self.opera_elements(element)
            return is_element
        except TimeoutException:
            return False

    def quick_is_elements(self, element, wait):
        # 快速判断多个元素是否存在
        try:
           time.sleep(wait)
           is_element = self.driver.find_elements(*element)
           return is_element
        except EC.NoSuchElementException:
            return False

    def quick_is_element(self, element, wait=1):
        # 快速判断元素是否存在
        try:
            time.sleep(wait)
            is_element =self.driver.find_element(*element)
            return is_element
        except EC.NoSuchElementException:
            return False

    def clear(self, element):
        # 清除元素文本内容
        is_element = self.opera_element(element)
        is_element.clear()

    def text_in_element(self, element, content: str):
        # 判断在规定的时间内元素是否包含content
        return self.action.until(EC.text_to_be_present_in_element(element, content),
                                 message=f'element: {element}  timeout...')

    def url_equal(self, url: str):
        # 判断浏览器当前中的url是否与url相等
        return self.action.until(EC.url_to_be(url), message=f'url: {url} timeout...')

    def url_contain(self, url: str):
        # 判断url在当前浏览器的url是否呈包含关系
        return self.action.until(EC.url_contains(url), message=f'url: {url} timeout...')

    def is_displayed(self, element):
        # 判断元素在规定的时间内是否显示，显示返回对应元素，不显示则返回False
        return self.action.until(EC.visibility_of_element_located(element),
                                 message=f'element: {element}  timeout...')

    def set_attributed(self, element, attribute_name: str, change_name: str):
        # 修改或者创建元素中属性的值
        is_element = self.opera_element(element)
        self.execute_js(f"arguments[0].setAttribute('{attribute_name}', '{change_name}');", is_element)

    def del_attributed(self, element, attribute_name: str):
        # 删除元素中属性
        is_element = self.opera_element(element)
        self.execute_js(f"arguments[0].removeAttribute('{attribute_name}');", is_element)

    def get_attributed(self, element, attribute_name: str):
        # 获取元素中其他属性值
        attribute_element = self.opera_element(element)
        return attribute_element.get_attribute(attribute_name)

    def attribute_value_in_text(self, element, text: str):
        # 判断元素中为“value”属性的值，是否包含text
        return self.action.until(EC.text_to_be_present_in_element_value(element, text),
                                 message=f'element: {element}  timeout...')
