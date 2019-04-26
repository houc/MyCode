import threading
import multiprocessing


class MyThread(threading.Thread):
    """
    字典的形式传送：key为function，value为function参数
    如:不带参数传入{get_log: (), current_file_path: ()}
    如:带参数传入{get_log: ('黄雄安', 'hello', 6), current_file_path: (5)}
    """
    def __init__(self, *args):
        threading.Thread.__init__(self)
        if args:
            self.function_message = list(args)[0]
        else:
            raise ValueError('args is none')

    def _method_conversion_list(self):
        """多个方法进行封装"""
        thread = []
        if isinstance(self.function_message, dict) and self.function_message:
            for fun, value in self.function_message.items():
                thread.append(threading.Thread(target=fun, args=value))
            return thread
        else:
            raise TypeError('Type not is dict or args is none')

    def run(self, switch=True):
        """执行所有方法中的功能"""
        for fun in self._method_conversion_list():
            fun.start()
            if switch:
                fun.join()


class MyProcess(object):
    def __init__(self, func, parm=()):
        self._run(func, parm)

    def _run(self, func, parm=()):
        """执行多进程运行"""
        loop = multiprocessing.Pool()
        loop.map_async(func=func, iterable=parm)
        loop.close()
        loop.join()
