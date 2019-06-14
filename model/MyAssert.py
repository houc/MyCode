import re

from config_path.path_file import read_file
from model.MyDB import MyDB
from model.SQL import Mysql
from model.Yaml import MyConfig
from model.TimeConversion import standard_time


class MyAsserts():
    def __init__(self, first, second, id, level, name, remark, status, reason, url, time,
                 driver, module, screenshots_path, author, myself, error_path, log=None,
                 encoding='utf8'):
        """初始化"""
        self.first = first
        self.second = second
        self.id = id
        self.level = level
        self.name = name
        self.remark = remark
        self.status = status
        self.reason = reason
        self.url = url
        self.time = time
        self.driver = driver
        self.screenshots_path = screenshots_path
        self.author = author
        self.myself = myself
        self.log = log
        self.error_path = error_path
        self.module = module
        self.encoding = encoding
        self.img_path = None
        self.thread = MyConfig('thread').config
        self.sql_type = MyConfig('execute_type').sql
        self.project = MyConfig('project_name').excel_parameter
        self.case_path = read_file(self.project, 'case.txt')
        if 'my_sql' == self.sql_type:
            self.sql = Mysql()
        else:
            self.sql = MyDB()

    def asserts(self):
        """用例断言"""
        self._exc(self.first, self.second, self.name)
        try:
            if self.reason is not None:
                if 'AssertionError' in self.reason:
                    self.status = '失败'
                else:
                    self.status = '错误'
                self.reason = self._strConversion(self.reason)
                self.img_path = self.screenshots_path
                self._log(self.reason)
            else:
                self.status = '成功'
                self.reason = self._strConversion(str(self.first))
        except Exception:
            raise
        finally:
            self._insert_sql(self.status, self.img_path, self.reason)

    def _insert_sql(self, status, img_path, reason):
        """将用例插入数据库,判断采用的数据库类型"""
        insert_time = standard_time()
        if self.thread:
            if 'my_sql' == self.sql_type:
                self.sql.insert_data(self.id, self.level, self.module, self.name, self._strConversion(self.remark),
                                     '{:.2f}秒'.format(self.time), status, self.url, insert_time,
                                     img_path, reason, self.author, results_value=self.second)
            else:
                case_data = {'id': self.id, 'level': self.level, 'module': self.module,
                             'name': self.name, 'mark': self._strConversion(self.remark),
                             'run_time': '{:.2f}秒'.format(self.time),'status': status, 'url': self.url,
                             'insert_time': insert_time, 'img_path': img_path, 'reason': reason,
                             'author': self.author, 'result': self.second}
                with open(self.case_path, 'at', encoding=self.encoding) as f:
                    f.write(str(case_data) + '\n')
        else:
            self.sql.insert_data(self.id, self.level, self.module, self.name, self._strConversion(self.remark),
                                 '{:.3f}秒'.format(self.time), status, self.url, insert_time,
                                 img_path, reason, self.author, results_value=self.second)

    @staticmethod
    def _strConversion(values: str):
        """字符串中包含单引号转义成``"""
        return re.sub("'", "`", values).replace('\\', '/')

    def _log(self, reason):
        """记录日志"""
        self.log.logging_debug('执行时间:{},错误路径:{},错误原因:{}'.
                               format(standard_time(), self.error_path, reason))
    @staticmethod
    def _exc(first, second, case_name):
        """异常判断"""
        if first is None and second is None:
            import warnings
            warnings.warn('请检查用例:{}，是否定义Element...'.format(case_name))
