import logging
import time
import sys
import os

from datetime import datetime, timedelta
from config_path.path_file import read_file
from model.Yaml import MyConfig
from model.TimeConversion import standard_time


class Logger:
    def __init__(self, encoding='utf-8'):
        """初始化"""
        formatter = logging.Formatter()
        now_time = time.strftime('%Y-%m-%d')
        dir_log = '{}.log'.format(now_time)
        log_dir = read_file('log', dir_log)
        level = MyConfig('level').config
        logs_day = MyConfig('logs_save').config
        file_handler = logging.FileHandler(log_dir, encoding=encoding)
        file_handler.setFormatter(formatter)
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.formatter = formatter
        self.Logging = logging.getLogger(__name__)
        self.Logging.addHandler(file_handler)
        self.Logging.setLevel(level)
        self.current_time = standard_time()
        if isinstance(logs_day, int):
            for i in range(logs_day):
                dir_log = '{}.log'.format((datetime.today() - timedelta(days=i + logs_day)).strftime('%Y-%m-%d'))
                log_dir = read_file('log', dir_log)
                exists = os.path.exists(log_dir)
                if exists:
                    os.remove(log_dir)
        else:
            TypeError('日志最长保存天数格式错误，它需要是一个int型')

    def logging_error(self, content):
        """错误日志"""
        self.Logging.error(content)

    def logging_debug(self, content):
        """debug日志"""
        self.Logging.debug('[{}]->>'.format(self.current_time) + content)

    def logging_info(self, content):
        """日志详情"""
        self.Logging.info(content)


if __name__ == '__main__':
    logging_test = Logger()
