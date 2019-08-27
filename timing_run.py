import schedule
import dataclasses
import os
import re

from model.Yaml import MyConfig

TIMES = MyConfig('task_time').config
PATH = os.path.dirname(__file__)


@dataclasses.dataclass
class TimingRunning:
    def __post_init__(self):
        self.runner = os.path.join(PATH, 'runner.py').replace('\\', '/')

    def __implement(self):
        return os.system(self.runner)

    def __time_conversion_is_list(self, parameter: list):
        for param in parameter:
            if isinstance(param, str):
                times = int(re.split('[a-z]', param)[0])
                units = ''.join(re.findall('[a-z]|[|]\d+:\d+', param))
                unit = re.split('[|]', units)
                if unit[0] == 's': schedule.every(times).seconds.do(self.__implement)
                if unit[0] == 'min': schedule.every(times).minutes.do(self.__implement)
                if unit[0] == 'h': schedule.every(times).hours.do(self.__implement)
                if unit[0] == 'day': schedule.every(times).day.at(unit[1]).do(self.__implement)
                if unit[0] == 'week': schedule.every(times).weeks.do(self.__implement)
                if unit[0] == 'monday': schedule.every().monday.at(unit[1]).do(self.__implement)
                if unit[0] == 'tuesday': schedule.every().tuesday.at(unit[1]).do(self.__implement)
                if unit[0] == 'wednesday': schedule.every().wednesday.at(unit[1]).do(self.__implement)
                if unit[0] == 'thursday': schedule.every().thursday.at(unit[1]).do(self.__implement)
                if unit[0] == 'friday': schedule.every().friday.at(unit[1]).do(self.__implement)
                if unit[0] == 'saturday': schedule.every().saturday.at(unit[1]).do(self.__implement)
                if unit[0] == 'sunday': schedule.every().sunday.at(unit[1]).do(self.__implement)
                else: schedule.every(times).minutes.do(self.__implement)
            else: schedule.every(param).minutes.do(self.__implement)

    def job(self):
        if isinstance(TIMES, list):
            self.__time_conversion_is_list(TIMES)
        if isinstance(TIMES, int):
            # 可自行增加对应规则！
            schedule.every(TIMES).minutes.do(self.__implement)
        if isinstance(TIMES, str):
            # 可自行增加对应规则！
            schedule.every().days.at(TIMES).do(self.__implement)


if __name__ == '__main__':
    if TIMES:
        TimingRunning().job()
        while True:
            schedule.run_pending()


