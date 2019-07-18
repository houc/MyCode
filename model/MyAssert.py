import re

from model.MyDB import MyDB
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
        self.project = MyConfig('project_name').excel_parameter

    def asserts(self):
        """用例断言"""
        if self.reason is not None:
            if 'AssertionError' in str(self.reason):
                self.status = '失败'
            else:
                self.status = '错误'
            self.reason = self._strConversion(str(self.reason))
            self.img_path = self.screenshots_path
            self._log(self.reason)
        else:
            self.status = '成功'
            self.reason = self._strConversion(str(self.first))
        self._insert_sql(self.status, self.img_path, self.reason)

    def _insert_sql(self, status, img_path, reason):
        """将用例插入数据库,判断采用的数据库类型"""
        insert_time = standard_time()
        MyDB().insert_data(self.id, self.level, self.module, self.name, self._strConversion(self.remark),
                             '{:.2f}秒'.format(self.time), status, self.url, insert_time,
                             img_path, reason, self.author, results_value=self.second)

    @staticmethod
    def _strConversion(values: str):
        """字符串中包含单引号转义成``"""
        return re.sub("'", "`", values).replace('\\', '/').replace('"', "`")

    def _log(self, reason):
        """记录日志"""
        self.log.logging_debug(f'执行时间:{standard_time()},错误路径:{self.error_path},错误原因:{reason}')

