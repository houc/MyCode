import inspect

def _get_function_name():
    """获取方法名称"""
    return inspect.stack()[1][3]

def _Exception():
    return Exception

FUN_NAME = _get_function_name
_EXCEPTION = _Exception()

class RequestsError(_EXCEPTION):
    """
        当接口发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, interface_name, back_message):
        self.interface_name = interface_name
        self.back_message = back_message

    def __str__(self):
        return "接口{!r}-请求失败，失败原因:{!r}".format(self.interface_name, self.back_message)


class AssertParams(_EXCEPTION):
    """
        当断言参数发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name, assert_first, assert_second):
        self.assert_first = assert_first
        self.assert_second = assert_second
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},断言:{!r}不存在或者断言:{!r}不存在".format(self.module_name, self.assert_first, self.assert_second)


class WaitTypeError(_EXCEPTION):
    """
        当浏览器等待参数发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},等待时间格式错误,格式应该为int类型".format(self.module_name)


class SQLDataError(_EXCEPTION):
    """
        当SQL数据为空时时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},SQL数据库为空数据,未能生成Excel测试报告".format(self.module_name)


class TypeErrors(_EXCEPTION):
    """
        类型有误时，调用该方法，即可返回错误的信息到控制台!
    """
    def __init__(self, module_name):
        self.module_name = module_name

    def __str__(self):
        return "模块:{!r},类型错误,请更正".format(self.module_name)

class LogErrors(_EXCEPTION):
    """
        记录错误日志到日志中!
    """
    def __init__(self, module_name, current_time, reason):
        self.module_name = module_name
        self.reason = reason
        self.time = current_time

    def __str__(self):
        return "执行时间:{},模块:{!r},错误原因:{}".format(self.time, self.module_name, self.reason)