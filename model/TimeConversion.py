import time
import os

from datetime import datetime, timedelta
from model.MyException import TypeErrors, FUN_NAME

PATH = os.path.dirname(__file__)


def standard_time():
    """返回当前标准的时间"""
    return time.strftime(_format())


def timestamp_time(second=1):
    """返回当前时间戳"""
    standard = standard_time()
    now_time = int(time.mktime(time.strptime(standard, _format()))) * second
    return now_time


def _format(switch=True):
    """格式化时间"""
    if switch:
        return '%Y-%m-%d %H:%M:%S'
    else:
        return '%Y%m%d%H%M%S'


def compact_time():
    """返回当前时间为紧凑型"""
    now_time = time.strftime(_format(False))
    return now_time


def custom_sub_time(custom):
    """当前时间减去自定义时间为天"""
    if isinstance(custom, int):
        sub_time = (datetime.now() - timedelta(days=custom)).strftime(_format())
        return sub_time
    else:
        raise TypeErrors(FUN_NAME(PATH))


def custom_add_time(custom):
    """当前时间加去自定义时间为天"""
    if isinstance(custom, int):
        sub_time = (datetime.now() + timedelta(days=custom)).strftime(_format())
        return sub_time
    else:
        raise TypeErrors(FUN_NAME(PATH))


def year_add_time(custom):
    """当前时间加上自定义时间为年"""
    if isinstance(custom, int):
        sub_time = (datetime.now() + timedelta(days=custom * 365)).strftime(_format())
        return sub_time
    else:
        raise TypeErrors(FUN_NAME(PATH))


def beijing_time_conversion_unix(beijing_time):
    """北京时间转换成时间戳时间"""
    return int(time.mktime(time.strptime(beijing_time, _format())))


def time_conversion(time):
    """根据秒数时间，推送具体的时间单位"""
    if 60 <= time <= 3600:
        return '{:.2f}'.format(time / 60) + '分钟'  # 计算的是分钟数，保留小数后2位数
    elif 3600 <= time <= 86400:
        return '{:.2f}'.format(time / 3600) + '小时'  # 计算的是小时，保留小数后2位数
    elif time <= 60:
        return '{:.2f}'.format(time) + '秒' # 计算的是秒，保留小数后2位数
    elif 86400 <= time:
        return '{:.2f}'.format(time / 86400) + '天' # 计算的是天，保留小数后2位数


if __name__ == '__main__':
    print(time_conversion(60.1))
