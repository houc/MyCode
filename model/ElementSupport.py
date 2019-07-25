import pykeyboard
import time

from PIL import ImageGrab
from selenium.webdriver.support.wait import WebDriverWait as Wait
from model.MyException import NoUrlTimeoutError


class GetCurrentUrl(object):
    def __call__(self, driver):
        return driver.current_url


class OtherOperationClass(object):
    def __init__(self, driver, timeout, detection, exception):
        self.driver = driver
        self.timeout = timeout
        self.keyboard = pykeyboard.PyKeyboard()
        self.ec_wait = Wait(driver=self.driver, timeout=self.timeout, poll_frequency=detection,
                            ignored_exceptions=exception)

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
        # 截屏当前屏幕（未执行selenium）
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

    def driver_quit(self):
        # 浏览器退出
        self.driver.quit()

    def screen_base64_shot(self):
        # 截屏浏览器操作屏幕（base64）
        return self.driver.get_screenshot_as_base64()

    def execute_js(self, js: str, *args):
        # 使用js操作浏览器
        return self.driver.execute_script(js, *args)

    def current_window(self):
        # 获取浏览器中当前操作窗口的句柄
        return self.driver.current_window_handle

    def more_window(self):
        # 获取浏览器全部操作窗口句柄
        return self.driver.window_handles

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

    def method_driver(self, method):
        # 定义driver继承
        return method(self.driver)

    def get_current_url(self):
        # 获取当前url
        url = GetCurrentUrl()
        return self.ec_wait.until(url, message=NoUrlTimeoutError(self.timeout))
