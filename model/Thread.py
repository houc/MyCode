import threading
import multiprocessing


class ExecuteThread(threading.Thread):
    def __init__(self, *args, parm=()):
        threading.Thread.__init__(self)
        self.function = args
        self.param = parm

    def _method_conversion_list(self):
        """多个方法进行封装"""
        thread = []
        if self.function:
            for funcs in self.function:
                if isinstance(funcs, list):
                    for fun in funcs:
                        thread.append(threading.Thread(target=fun))
                else:
                    thread.append(threading.Thread(target=funcs))
        return thread

    def run(self):
        """执行所有方法中的功能"""
        for i in self._method_conversion_list():
            i.setDaemon(daemonic=True)
            i.start()
            i.join(timeout=10)


class Process(object):
    def __init__(self, func, parm=()):
        self._run(func, parm)

    def _run(self, func, parm=()):
        """执行多进程运行"""
        loop = multiprocessing.Pool()
        loop.map_async(func=func, iterable=parm)
        loop.close()
        loop.join()
