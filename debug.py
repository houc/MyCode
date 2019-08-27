class Singleton(object):
    __instance = None                       # 定义实例

    def __init__(self):
        print(self.__instance)

    def __new__(cls, *args, **kwd):         # 在__init__之前调用
        if Singleton.__instance is None:    # 生成唯一实例
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance

Singleton()


class test():
    def __init__(self, k):
        self.k = k

    def __le__(self, other):
        return other <= self.k

test(21)


