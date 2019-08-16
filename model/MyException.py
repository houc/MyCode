import inspect
import traceback
import dataclasses
import json

def _get_function_name(path):
    """获取方法名称"""
    return path + '\\' + inspect.stack()[1][3]


FUN_NAME = _get_function_name


class RequestsError(Exception):
    """
        当接口发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, interface_name, back_message):
        self.interface_name = interface_name
        self.back_message = back_message

    def __str__(self):
        return "接口{!r}-请求失败，失败原因:{!r}".format(self.interface_name, self.back_message)


class AssertParams(Exception):
    """
        当断言参数发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name, assert_first, assert_second):
        self.assert_first = assert_first
        self.assert_second = assert_second
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},断言:{!r}不存在或者断言:{!r}不存在；或者用例中未定义元素执行".\
            format(self.module_name, self.assert_first, self.assert_second)


class WaitTypeError(Exception):
    """
        当浏览器等待参数发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},等待时间格式错误,格式应该为int类型".format(self.module_name)


class SQLDataError(Exception):
    """
        当SQL数据为空时时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},SQL数据库为空数据,未能生成Excel测试报告".format(self.module_name)


class TypeErrors(Exception):
    """
        类型有误时，调用该方法，即可返回错误的信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},类型错误,请更正".format(self.module_name)


class LogErrors(Exception):
    """
        记录错误日志到日志中!
    """
    def __init__(self, module_name, current_time, reason):
        self.module_name = module_name
        self.reason = reason
        self.time = current_time

    def __str__(self):
        return "执行时间:{},错误路径:{!r},错误原因:{}".format(self.time, self.module_name, self.reason)


class CreateFileError(Exception):
    """
        生成模板出现问题时，调用该异常!
    """

    def __init__(self, module_name, current_time, reason):
        self.module_name = module_name
        self.reason = reason
        self.time = current_time

    def __str__(self):
        return "执行时间:{},模块:{!r},错误原因:{}".format(self.time, self.module_name, self.reason)


class LoginError(Exception):
    """
        登录出现异常
    """
    def __init__(self, class_name, reason):
        self.class_name = class_name
        self.reason = reason

    def __str__(self):
        return "执行:{}时，在登录过程中遇到异常，测试被终止；异常原因:{}".format(self.class_name, self.reason)


class LoginSelectError(Exception):
    """
        登录出现公司异常
    """

    def __init__(self, class_name):
        self.class_name = class_name

    def __str__(self):
        return "执行:{}时，当in_login为True时，account或者password不能为None"


class SceneError(Exception):
    """
        场景错误
    """
    def __str__(self):
        return "common中scene参数为空，此参数不能为空，请增加"


class ExceptionPackage(object):
    """异常类的封装"""
    def __init__(self, module, driver, text=None):
        from model.Logs import logger
        error = traceback.format_exc()
        if text is None:
            logger.logging_debug(error)
            driver.quit()
        else:
            logger.logging_debug(text)
            driver.quit()


class ReadCommonError():
    def __init__(self, module, class_name, case_name):
        self.module = module
        self.class_name = class_name
        self.case_name = case_name

    def __str__(self):
        return "{}.{}.{}，场景中scene存在空数据，此项不能存在为空的数据，需修正...".\
                format(self.module, self.class_name, self.case_name, )


@dataclasses.dataclass
class UntilNoElementOrTimeoutError(Exception):
    timeout: float
    element: str

    def __str__(self):
        return f'元素: {self.element} 在DOM超时: {self.timeout}s 都未出现...'


@dataclasses.dataclass
class UntilNotNotElementOrTimeoutError(Exception):
    timeout: float
    element: str

    def __str__(self):
        return f'元素: {self.element} 在DOM超时: {self.timeout}s 都未消失...'


@dataclasses.dataclass
class NoUrlTimeoutError(Exception):
    timeout: float

    def __str__(self):
        return f'获取当前窗口url在 {self.timeout}s 都未能出现获取...'


@dataclasses.dataclass
class InterfaceEqErrors(Exception):
    module_name: str
    type: str
    url: str
    used_time: float
    status: int
    insert_data: str=None
    back_data: str=None
    remark: str=None

    def __str__(self):
        new_data_dict = {'except_msg': {
            'insert_data': {
                'module_name': self.module_name,
                'get_url': self.url,
                'pram': self.insert_data,
                'get_type': str(self.type).split(' ')[-1].split('>')[0]
            },
            'results': {
                'status_code': self.status,
                'used_time': self.used_time,
                'back_data': self.back_data
            },
            'remark': self.remark
        }}
        return json.dumps(obj=new_data_dict, indent=8, ensure_ascii=False)

