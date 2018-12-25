import inspect

def _get_fun_name():
    """获取方法名称"""
    return inspect.stack()[1][3]


class RequestsError(Exception):
    """
    当接口发生错误时，调用该方法，即可返回错误信息到控制台!
    """
    def __init__(self, interface_name, back_message):
        self.interface_name = interface_name
        self.back_message = back_message

    def __str__(self):
        return "接口{!r}-请求失败，失败原因:{!r}".format(self.interface_name, self.back_message)


FUN_NAME = _get_fun_name
