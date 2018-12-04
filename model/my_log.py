import logging,time,sys
from config_path.path_file import read_file
from yaml_read.read_yaml import MyYaml


class Logger:
    def __init__(self,encoding='utf-8'):
        """初始化"""
        formatter = logging.Formatter('TIME: %(asctime)s     ''DEF: %(funcName)s    ''MESSAGE：%(message)s     ' )
        now_time = time.strftime('%Y-%m-%d')
        dir_log = '{}.log'.format(now_time)
        log_dir = read_file('log', dir_log)
        level = MyYaml('level').config
        file_handler = logging.FileHandler(log_dir, encoding = encoding)
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
        console_handler = logging.StreamHandler(sys.stdout)  # 控制台日志
        console_handler.formatter = formatter
        self.Logging = logging.getLogger(__name__)
        self.Logging.addHandler(file_handler)
        self.Logging.setLevel(level)

    def logging_error(self,content):
        """错误日志"""
        self.Logging.error(content)

    def logging_debug(self,content):
        """debug日志"""
        self.Logging.debug(content)

    def logging_info(self,content):
        """日志详情"""
        self.Logging.info(content)

if __name__ == '__main__':
    logging_test = Logger()
    # logging_test.logging_error('错了')
    # logging_test.logging_debug('debug')
    logging_test.logging_info('08080808')