import time

from datetime import datetime, timedelta
from model.MyException import TypeErrors, FUN_NAME

def standard_time():
    """返回当前标准的时间"""
    now_time = time.strftime(_format())
    return now_time

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
        raise TypeErrors(FUN_NAME())

def custom_add_time(custom):
    """当前时间加去自定义时间为天"""
    if isinstance(custom, int):
        sub_time = (datetime.now() + timedelta(days=custom)).strftime(_format())
        return sub_time
    else:
        raise TypeErrors(FUN_NAME())

def year_add_time(custom):
    """当前时间加上自定义时间为年"""
    if isinstance(custom, int):
        sub_time = (datetime.now() + timedelta(days=custom * 365)).strftime(_format())
        return sub_time
    else:
        raise TypeErrors(FUN_NAME())

if __name__ == '__main__':
    print(custom_sub_time(999991))
