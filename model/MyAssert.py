import re

from model.MyDB import MyDB
from model.TimeConversion import standard_time, time_conversion


class MyAsserts():
    def __init__(self, first, second, id, level, name, remark, status, reason, url, time,
                 driver, module, screenshots_path, author, myself, error_path, log):
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
        self.img_path = None
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
                self._log(self.reason)
                self.reason = self._strConversion(self.reason)
                self.img_path = self.screenshots_path.replace('\\', '/')
                raise BaseException(self.reason)
            else:
                self.status = '成功'
                self.reason = self._strConversion(str(self.first))
        except Exception:
            raise
        finally:
            self._insert_sql(self.status, self.img_path, self.reason)

    def _insert_sql(self, status, img_path, reason):
        """将用例插入数据库"""
        insert_time = standard_time()
        self.sql.insert_data(self.id, self.level, self.module, self.name, self.remark, time_conversion(self.time),
                             status, self.url, insert_time, img_path, reason, self.author,
                             results_value=self.second)

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
