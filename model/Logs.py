import logging
import time
import os

from datetime import datetime, timedelta
from config_path.path_file import read_file
from model.Yaml import MyConfig


def _logger():
    logs_day = MyConfig('logs_save').config
    for i in range(logs_day):
        dir_log = '{}.log'.format((datetime.today() - timedelta(days=i + logs_day)).strftime('%Y-%m-%d'))
        log_dir = read_file('log', dir_log)
        exists = os.path.exists(log_dir)
        if exists:
            os.remove(log_dir)

    log_path = read_file('log', f'{time.strftime("%Y-%m-%d")}.log')
    logging.basicConfig(format="%(asctime)s %(filename)s: [%(levelname)s]: %(message)s",
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S -> %A || -> ',
                        filename=log_path,
                        filemode='a+')
    return logging


logger = _logger()


