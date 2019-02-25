import os
import re
import traceback

from model.SQL import Mysql
from model.TimeConversion import standard_time
from model.MyException import AssertParams


class MyAsserts():
    def __init__(self, first, second, id, level, name, remark, status, reason, url, time,
                 driver, module, screenshots_path, author, myself, error_path, log, results_value,):
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
        self.results_value = results_value
        self.module = module
        self.img_path = None
        self.sql = Mysql()

    def asserts(self):
        """判断first与second值是否相等"""
        try:
            if self.first and self.second is not None:
                if isinstance(self.first, type(self.second)):
                    if self.first == self.second:
                        self.status = '成功'
                        self._assert()
                    elif not self.first == self.second:
                        self.status = '失败'
                        self.driver.save_screenshot(self.screenshots_path)
                        first = self._strConversion(str(self.first))
                        second = self._strConversion(str(self.second))
                        self.reason = '"%s" != "%s"' % (first, second)
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        self._assert()
                    if self.reason is not None:
                        self.status = '错误'
                        self.driver.save_screenshot(self.screenshots_path)
                        reason = self._strConversion(str(self.reason))
                        self.reason = reason
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        try:
                            raise BaseException(self.reason)
                        finally:
                            self._log(self.reason)
                            self._assert()
                else:
                    if str(self.first) == str(self.second):
                        self.status = '成功'
                        self._assert()
                    elif not str(self.first) == str(self.second):
                        self.status = '失败'
                        first = self._strConversion(str(self.first))
                        second = self._strConversion(str(self.second))
                        self.reason = '"%s" != "%s"' % (first, second)
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        self._assert()
            else:
                if self.reason is not None:
                    self.status = '错误'
                    self.driver.save_screenshot(self.screenshots_path)
                    reason = self._strConversion(str(self.reason))
                    self.reason = reason
                    if os.path.exists(self.screenshots_path):
                        self.img_path = str(self.screenshots_path).replace('\\', '/')
                    self._log(self.reason)
                    try:
                        raise BaseException(self.reason)
                    finally:
                        self._log(self.reason)
                        self._assert()
                if isinstance(self.first, type(self.second)):
                    if isinstance(self.first and self.second, bool):
                        if self.first == self.second:
                            self.status = '成功'
                            self._assert()
                        elif not self.first == self.second:
                            self.status = '失败'
                            self.driver.save_screenshot(self.screenshots_path)
                            first = self._strConversion(str(self.first))
                            second = self._strConversion(str(self.second))
                            self.reason = '"%s" != "%s"' % (first, second)
                            if os.path.exists(self.screenshots_path):
                                self.img_path = str(self.screenshots_path).replace('\\', '/')
                            self._log(self.reason)
                            self._assert()
                    else:
                        if self.reason is not None:
                            try:
                                raise AssertParams(self.error_path, 'self.first', 'self.second', 'self.error')
                            finally:
                                self._log(traceback.format_exc())
                        self._assert()
                else:
                    try:
                        raise AssertParams(self.error_path, 'self.first', 'self.second', 'self.error')
                    finally:
                        self._log(traceback.format_exc())
        finally:
            self._insert_sql(self.status, self.img_path, self.reason)

    def _insert_sql(self, status, img_path, reason):
        """将用例插入数据库"""
        insert_time = standard_time()
        self.sql.insert_data(self.id, self.level, self.module, self.name, self.remark, "{:.4f}s".format(self.time),
                             status,self.url, insert_time, img_path, reason, self.author,
                             results_value=self.results_value)

    @staticmethod
    def _strConversion(values: str):
        """字符串中包含单引号转义成``"""
        res = re.sub("'", "`", values)
        return res

    def _log(self, reason):
        """记录日志"""
        self.log.logging_debug('执行时间:{},错误路径:{},错误原因:{}'.
                               format(standard_time(), self.error_path, reason))

    def _assert(self):
        """断言"""
        self.myself.assertEqual(self.first, self.second, msg=self.reason)

