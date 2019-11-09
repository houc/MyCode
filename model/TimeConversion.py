import time
import os

from datetime import datetime, timedelta
from model.MyException import TypeErrors, FUN_NAME

PATH = os.path.dirname(__file__)
BEIJING_FORMAT = '%Y-%m-%d %H:%M:%S'
MERGE_FORMAT = '%Y%m%d%H%M%S'
TIME_FORMAT = '%H:%M:%S'
YEAR_FORMAT = '%Y-%m-%d'


def timestamp_time(second=1):
    """返回当前时间戳"""
    standard = standard_time()
    now_time = int(time.mktime(time.strptime(standard, BEIJING_FORMAT))) * second
    return now_time


def compact_time():
    """返回当前时间为紧凑型"""
    now_time = time.strftime(MERGE_FORMAT)
    return now_time


def custom_sub_time(custom):
    """当前时间减去自定义时间为天"""
    if isinstance(custom, int):
        sub_time = (datetime.now() - timedelta(days=custom)).strftime(BEIJING_FORMAT)
        return sub_time
    else:
        raise TypeErrors(FUN_NAME(PATH))


def custom_add_time(custom):
    """当前时间加去自定义时间为天"""
    if isinstance(custom, int):
        sub_time = (datetime.now() + timedelta(days=custom)).strftime(BEIJING_FORMAT)
        return sub_time
    else:
        raise TypeErrors(FUN_NAME(PATH))


def year_add_time(custom):
    """当前时间加上自定义时间为年"""
    if isinstance(custom, int):
        sub_time = (datetime.now() + timedelta(days=custom * 365)).strftime(BEIJING_FORMAT)
        return sub_time
    else:
        raise TypeErrors(FUN_NAME(PATH))


def beijing_time_conversion_unix(beijing_time):
    """北京时间转换成时间戳时间"""
    return int(time.mktime(time.strptime(beijing_time, BEIJING_FORMAT)))


def time_conversion(time):
    """根据秒数时间，推送具体的时间单位"""
    if not isinstance(time, (int, float)):
        raise TypeError(f'参数 "time {time!r}" , 只能为int类型或者float类型')
    if 60 <= time <= 3600:
        return f'{(time / 60):.2f}分钟'  # 计算的是分钟数，保留小数后2位数
    elif 3600 <= time <= 86400:
        return f'{(time / 3600):.2f}小时'  # 计算的是小时，保留小数后2位数
    elif time <= 60:
        return f'{time:.2f}秒' # 计算的是秒，保留小数后2位数
    elif 86400 <= time:
        return f'{(time / 86400):.2f}天' # 计算的是天，保留小数后2位数


def standard_time(formats=BEIJING_FORMAT):
    """返回当前标准的时间"""
    return time.strftime(formats)


def return_y_d_m(starts_year_time=10, ends_day_time=10):
    """返回时间区间年月日"""
    assert starts_year_time > 0, '开始年限不可小于0、、、'
    time_type = datetime.strptime(standard_time(YEAR_FORMAT), YEAR_FORMAT)
    y, m, d = time_type.year - starts_year_time, time_type.month, time_type.day
    starts_year = datetime(y, m, d).strftime(YEAR_FORMAT)
    format_start_year = datetime.strptime(starts_year, YEAR_FORMAT)
    format_end_year = (datetime.today() - timedelta(days=ends_day_time))
    while format_start_year < format_end_year:
        format_start_year += timedelta(days=1)
        yield format_start_year.strftime(YEAR_FORMAT)


if __name__ == '__main__':
    for a in return_y_d_m(1, 10):
        print(a)