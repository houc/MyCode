import dataclasses
import webbrowser

from selenium.webdriver.common.action_chains import ActionChains as Opera
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from model.ElementSupport import OtherOperationClass
from model.MyException import (UntilNoElementOrTimeoutError,
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
    driver: webbrowser
    timeout: float
    detection: float
    exception: EC

    def __post_init__(self):
        super(_MouseToOperations, self).__post_init__()
        self.mouse_support = Opera(self.driver)

    def drag_and_drop(self, source_element, target_elemet):
        """
        将单个元素进行拖拽到另一个元素中
        :param source: 执行拖拽的元素
        :param target: 到另一个元素位置
        """
        source = self.opera_element(source_element)
        target = self.opera_element(target_elemet)
        self.mouse_support.drag_and_drop(source=source, target=target).perform()

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
        双击元素
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.double_click(on_element=is_element).perform()

    def right_click(self, element):
        """
        右键元素
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.context_click(on_element=is_element).perform()

    def click(self, element):
        """
        左键单击元素
        :param element: (By.XPATH, "//div[text()='百度一下']")
        """
        is_element = self.opera_element(element)
        self.mouse_support.click(on_element=is_element).perform()


class OperationElement(_MouseToOperations, OtherOperationClass):
    # 浏览器所需元素操作方法封装类

    def __init__(self, driver, timeout=5, detection=0.5, exception=EC.NoSuchElementException):
        super(_MouseToOperations, self).__init__(driver=driver, timeout=timeout,
                                                 detection=detection, exception=exception)
        OtherOperationClass.__init__(self, driver=driver, timeout=timeout,
                                     detection=detection, exception=exception)
        self.driver = driver

    def switch_iframe(self, frame_element):
        # 切换到iframe的dom上
        iframe = self.ec_wait.until(EC.frame_to_be_available_and_switch_to_it(frame_element),
                                    message=f'iframe_element:  {frame_element}  timeout...')
        if not iframe:
            raise EC.NoSuchFrameException(f'switch {frame_element} it failed！')

    def is_click(self, element):
        # 执行元素可见点击操作
        clicked = self.ec_wait.until(EC.element_to_be_clickable(element),
                                     message=f'element: {element}  timeout...')
        if clicked:
            clicked.click()
        else:
            raise EC.NoSuchElementException(f'element: {element}  Not visible or enabled...')

    def is_send(self, element, value: str):
        # 元素是否可输入对应内容
        is_element = self.opera_element(element)
        is_element.send_keys(value)

    def is_submit(self, element):
        # 元素是否可提交
        is_element = self.opera_element(element)
        is_element.submit()

    def is_text(self, element):
        # 获取元素中文本值
        is_element = self.opera_element(element)
        return is_element.text

    def is_element(self, element):
        # 判断元素是否存在
        try:
            self.opera_element(element)
            return True
        except TimeoutError:
            return False

    def is_clear(self, element):
        # 清除元素文本内容
        is_element = self.opera_element(element)
        is_element.clear()

    def is_in_text(self, element, content: str):
        # 判断元素是否包含content
        return self.ec_wait.until(EC.text_to_be_present_in_element(element, content),
                                  message=f'element: {element}  timeout...')

    def is_url_equal(self, url: str):
        # 判断浏览器当前中的url是否与url相等
        return self.ec_wait.until(EC.url_to_be(url), message=f'url: {url} timeout...')

    def is_url_contain(self, url: str):
        # 判断url在当前浏览器的url是否呈包含关系
        return self.ec_wait.until(EC.url_contains(url), message=f'url: {url} timeout...')

    def is_displayed(self, element):
        # 判断元素是否显示，显示返回对应元素，不显示则返回False
        return self.ec_wait.until(EC.visibility_of_element_located(element),
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

    def is_attributed(self, element, text: str, attribute_name: str):
        # 判断属性中是否包含text内容
        attribute_element = self.opera_element(element)
        return text in attribute_element.get_attribute(attribute_name)

    def is_attribute_value(self, element, text: str):
        # 判断元素中为“value”属性的值，是否包含text
        return self.ec_wait.until(EC.text_to_be_present_in_element_value(element, text),
                                  message=f'element: {element}  timeout...')