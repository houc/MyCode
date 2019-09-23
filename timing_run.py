import schedule
import dataclasses
import os
import re
import sys

from model.Yaml import MyConfig

TIMES = MyConfig('task_time').config
PATH = os.path.abspath('.')


@dataclasses.dataclass
class TimingRunning:
    def __post_init__(self):
        self.runner = os.path.join(PATH, 'runner.py').replace('\\', '/')

    def __implement(self):
        return os.system(self.runner)

    def __time_conversion_is_list(self, parameter: list):
        for param in parameter:
            if isinstance(param, str):
                times = int(re.split('[(a-z)]', param)[0])
                scheduled = schedule.every(times)
                units = ''.join(re.findall('[a-z]|[|]\d+:\d+', param))
                if '|' in units: unit = re.split('[|]', units)
                else: unit = units
                if isinstance(unit, list): times, unit = unit[1], unit[0]
                if unit == 's':
                    scheduled.seconds.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'min':
                    scheduled.minutes.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'h':
                    scheduled.hours.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'day':
                    if not isinstance(times, int): scheduled.days.at(times).do(self.__implement)
                    else: scheduled.days.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'week':
                    scheduled.weeks.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'monday':
                    if not isinstance(times, int): scheduled.monday.at(times).do(self.__implement)
                    else:scheduled.monday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'tuesday':
                    if not isinstance(times, int): scheduled.tuesday.at(times).do(self.__implement)
                    else: scheduled.tuesday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'wednesday':
                    if not isinstance(times, int): scheduled.wednesday.at(times).do(self.__implement)
                    else: scheduled.wednesday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'thursday':
                    if not isinstance(times, int): scheduled.thursday.at(times).do(self.__implement)
                    else: scheduled.thursday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'friday':
                    if not isinstance(times, int): scheduled.friday.at(times).do(self.__implement)
                    else: scheduled.friday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'saturday':
                    if not isinstance(times, int): scheduled.saturday.at(times).do(self.__implement)
                    else: scheduled.saturday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')
                if unit == 'sunday':
                    if not isinstance(times, int): scheduled.sunday.at(times).do(self.__implement)
                    else: scheduled.sunday.do(self.__implement)
                    sys.stderr.write(f'已启动定时{unit!r}, {times!r}滴任务...')

    def job(self):
        if isinstance(TIMES, list):
            self.__time_conversion_is_list(TIMES)
        if isinstance(TIMES, int):
            # 可自行增加对应规则！
            schedule.every(TIMES).minutes.do(self.__implement)
            sys.stderr.write(f'已启动每{TIMES!r}分钟定时任务...')
        if isinstance(TIMES, str):
            # 可自行增加对应规则！
            schedule.every().days.at(TIMES).do(self.__implement)
            sys.stderr.write(f'已启动每天执行, {TIMES!r}滴任务...')
        sys.stderr.flush()


if __name__ == '__main__':
    if TIMES:
        TimingRunning().job()
        while True:
            schedule.run_pending()


