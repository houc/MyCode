import time
import pykeyboard
import pymouse

from selenium.webdriver.common.action_chains import ActionChains as hover
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from model.DriverParameter import browser
from model.Yaml import MyConfig
from PIL import ImageGrab


class OperationElement(object):
    def __init__(self, driver, timeout=5, detection=0.2, exception=EC.NoSuchElementException):
        self.driver = driver
        self.key = pykeyboard.PyKeyboard()
        self.mouse = pymouse.PyMouse()
        self.support = Wait(driver=self.driver, timeout=timeout, poll_frequency=detection,
                            ignored_exceptions=exception)

    def f5(self):
        # 刷新浏览器
        self.driver.refresh()

    def get(self, url: str):
        # 请求需访问的地址
        self.driver.get(url)

    def drag(self, source, target):
        # 单个元素进行拖拽到另一个元素中
        element_source = self.operation_element(source)
        element_target = self.operation_element(target)
        hover(self.driver).drag_and_drop(element_source, element_target).perform()

    def drag_offset(self, element, x_offset, y_offset):
        # 单个元素进行拖拽到指定的x坐标和y坐标位置
        is_element = self.operation_element(element)
        hover(self.driver).drag_and_drop_by_offset(is_element, x_offset, y_offset).perform()

    def driver_quit(self):
        # 浏览器退出
        self.driver.quit()

    @staticmethod
    def open_browser():
        # 重新打开浏览器
        headless = MyConfig('browser').config
        return browser(switch=headless)

    @staticmethod
    def full_window_screen(path: str, length=None, height=None):
        # 截屏当前屏幕（未执行selenium）
        screen = ImageGrab.grab()
        if length is not None and height is not None:
            screen.size = length, height
        screen.save(path)

    def screen_base64_shot(self):
        # 截屏浏览器操作屏幕（base64）
        return self.driver.get_screenshot_as_base64()

    def execute_js(self, js: str, *args):
        # 使用js操作浏览器
        return self.driver.execute_script(js, *args)

    def current_window(self):
        # 获取浏览器中当前操作窗口的句柄
        return self.driver.current_window_handle

    def hovers(self, element):
        # 悬浮到某一个元素上
        hover_element = self.operation_element(element)
        hover(self.driver).move_to_element(hover_element).perform()

    def more_window(self):
        # 获取浏览器全部操作窗口句柄
        return self.driver.window_handles

    def switch_window(self, indexes: int):
        # 切换浏览器窗口句柄
        window = self.more_window()
        return self.driver.switch_to.window(window[indexes])

    def switch_frame(self, frame_reference: str):
        # 切换到ifr的dom上
        return self.driver.switch_to.frame(frame_reference)

    def release_frame(self):
        # 回跳至默认dom上
        return self.driver.switch_to.default_content()

    def close_current_window(self):
        # 关闭当前浏览器窗口
        self.driver.close()
    
    def operation_element(self, element):
        # 对元素进行判断是否存在
        return self.support.until(EC.presence_of_element_located(element),
                                  message=f'元素: {element}  超时...')

    def operation_elements(self, elements):
        # 对多个元素进行判断是否存在
        return self.support.until(EC.presence_of_all_elements_located(elements),
                                  message=f'元素: {elements}  超时...')

    def is_click(self, element):
        # 执行点击操作
        is_click = self.support.until(EC.element_to_be_clickable(element),
                                      message=f'元素: {element}  超时...')
        if is_click:
            is_click.click()
        else:
            raise TimeoutError(f'元素: {element}  不可见或者未启用...')

    def script_upload(self, path: str):
        # 采用PyUserInput，上传附件可避免非input标签进行上传附件
        time.sleep(1)
        self.key.tap_key(self.key.shift_key)
        self.key.type_string(path.replace('/', '\\'))
        time.sleep(1)
        self.key.tap_key(self.key.enter_key)

    def script_click(self, x: int, y: int, button: int=1, n: int=1):
        # 采用PyUserInput，执行点击操作
        self.mouse.click(x, y, button, n)

    def method_driver(self, method):
        # 定义一个driver继承
        return method(self.driver)

    def is_send(self, element, value):
        # 输入对应内容
        is_element = self.operation_element(element)
        is_element.send_keys(value)

    def is_text(self, element):
        # 获取元素中文本值
        is_element = self.operation_element(element)
        return is_element.text

    def is_attributed(self, element, text, value):
        # 判断属性中是否包含text内容
        attribute_element = self.operation_element(element)
        return text in attribute_element.get_attribute(value)

    def get_attributed(self, element, value):
        # 获取元素中其他属性值
        attribute_element = self.operation_element(element)
        return attribute_element.get_attribute(value)

    def is_element(self, element):
        # 判断元素是否存在
        try:
            self.operation_element(element)
            return True
        except TimeoutError:
            return False

    @staticmethod
    def str_conversion(element, *args):
        # 参数转化
        if "$" in element[1]:
            now_value = element[1].replace("$", "{}")
            new_element = (element[0], now_value.format(*args))
            return new_element
        else:
            raise ValueError('无需参数化，请不要调用该方法，或者参数化需要“$”')

    def is_in_text(self, element, content: str):
        # 判断元素是否包含content
        return self.support.until(EC.text_to_be_present_in_element(element, content),
                                  message=f'元素: {element}  超时...')

    def is_url_equal(self, url: str):
        # 判断浏览器当前中的url是否与url相等
        return self.support.until(EC.url_to_be(url), message=f'url: {url} 超时...')

    def get_url(self):
        # 获取浏览器当前中的url
        url = _Get()
        return self.support.until(url, message=f'url: {url} 超时...')

    def is_url_contain(self, url: str):
        # 判断url在当前浏览器的url是否呈包含关系
        return self.support.until(EC.url_contains(url), message=f'url: {url} 超时...')

    def is_attribute_value(self, element, text: str):
        # 判断元素中为“value”属性的值，是否包含text
        return self.support.until(EC.text_to_be_present_in_element_value(element, text),
                                  message=f'元素: {element}  超时...')

    def is_displayed(self, element):
        # 判断元素是否显示
        return self.support.until(EC.visibility_of_element_located(element),
                                  message=f'元素: {element}  超时...')

    def change_element_value(self, element, attribute_name: str, change_name: str):
        # 修改元素中属性的值
        is_element = self.operation_element(element)
        self.execute_js(f"arguments[0].setAttribute('{attribute_name}', '{change_name}');", is_element)


class _Get(object):
    def __call__(self, driver):
        return driver.current_url

