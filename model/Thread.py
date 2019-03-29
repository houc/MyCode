import threading


class ExecuteThread(threading.Thread):
    """
    usage:
        不带参数:ExecuteThread([func_1, func_2, func_3]).run()
        带参数:ExecuteThread([func_1, func_2, func_3], []).run()
    """
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        self.function = args
        self.param = kwargs

    def _method_conversion_list(self):
        """多个方法进行封装"""
        Thread = []
        if self.function:
            for funcs in self.function:
                if isinstance(funcs, list):
                    for fun in funcs:
                        Thread.append(threading.Thread(target=fun))
                else:
                    Thread.append(threading.Thread(target=funcs))
        return Thread

    def run(self):
        """执行所有方法中的功能"""
        for i in self._method_conversion_list():
            i.setDaemon(daemonic=True)
            i.start()
            i.join(timeout=10)

