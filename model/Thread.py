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

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        fun = [runner, runr]
        for a in fun:
            m = threading.Thread(target=a)
            m.start()
import time

def runner():
    one().test_1()
    one().test_2()

def runr():
    two().test_3()
    two().test_4()

class one():
    def test_1(self):
        time.sleep(1)
        print('test_1')

    def test_2(self):
        time.sleep(1)
        print('test_2')

class two():
    def test_3(self):
        time.sleep(1)
        print('test_3')

    def test_4(self):
        time.sleep(1)
        print('test_4')

if __name__ == '__main__':
    loop = myThread()
    loop.start()
