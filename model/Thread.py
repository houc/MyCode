import threading


class ExecuteThread(threading.Thread):
    def __init__(self, method=list()):
        threading.Thread.__init__(self)
        self.method = method

    def _method_conversion_list(self):
        """多个方法进行封装"""
        Thread = list()
        if isinstance(self.method, list):
            for i in self.method:
                thread = threading.Thread(target=i)
                Thread.append(thread)
            return Thread

    def run(self):
        """执行所有方法中的功能"""
        for i in self._method_conversion_list():
            i.setDaemon(daemonic=True)
            i.start()
            i.join(timeout=10)

