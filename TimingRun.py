import schedule
import os

from model.Yaml import MyYaml


class Timing:
    def __init__(self):
        """初始化"""
        path = os.path.dirname(__file__)
        self.runner = os.path.join(path, 'runner.py').replace('\\', '/')
        self.times = MyYaml('task_time').config

    def implement(self):
        """执行模块"""
        return os.system(self.runner)

    def job(self):
        """执行时间"""
        if isinstance(self.times, int):
            schedule.every(self.times).minutes.do(self.implement)
        else:
            TypeError("task_time need int type")

if __name__ == '__main__':
    Timing().job()
    while True:
        schedule.run_pending()