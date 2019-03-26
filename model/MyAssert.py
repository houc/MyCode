import os
import re
import traceback

from model.MyDB import MyDB
from model.TimeConversion import standard_time
from model.MyException import AssertParams


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

    def asserts_eq(self):
        """判断first与second值是否相等"""
        try:
            if self.first and self.second is not None:
                if isinstance(self.first, type(self.second)):
                    if self.first == self.second:
                        self.status = '成功'
                        self.reason = self._strConversion(str(self.first))
                        self._assert_eq()
                    elif not self.first == self.second:
                        self.status = '失败'
                        first = self._strConversion(str(self.first))
                        second = self._strConversion(str(self.second))
                        self.reason = '"%s" 不等于 "%s"' % (first, second)
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        self._assert_eq()
                else:
                    if str(self.first) == str(self.second):
                        self.status = '成功'
                        self.reason = self._strConversion(str(self.first))
                        self._assert_eq()
                    elif not str(self.first) == str(self.second):
                        self.status = '失败'
                        first = self._strConversion(str(self.first))
                        second = self._strConversion(str(self.second))
                        self.reason = '"%s" 不等于 "%s"' % (first, second)
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        self._assert_eq()
                    elif self.reason is not None:
                        self.status = '错误'
                        reason = self._strConversion(str(self.reason))
                        self.reason = reason
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        try:
                            raise BaseException(self.reason)
                        finally:
                            self._log(self.reason)
            else:
                if self.reason is not None:
                    self.status = '错误'
                    self.reason = self._strConversion(str(self.reason))
                    if os.path.exists(self.screenshots_path):
                        self.img_path = str(self.screenshots_path).replace('\\', '/')
                    self._log(self.reason)
                    try:
                        raise BaseException(self.reason)
                    finally:
                        self._log(self.reason)
                if isinstance(self.first, type(self.second)):
                    if isinstance(self.first and self.second, bool):
                        if self.first == self.second:
                            self.status = '成功'
                            self.reason = self._strConversion(str(self.first))
                            self._assert_eq()
                        elif not self.first == self.second:
                            self.status = '失败'
                            first = self._strConversion(str(self.first))
                            second = self._strConversion(str(self.second))
                            self.reason = '"%s" 不等于 "%s"' % (first, second)
                            if os.path.exists(self.screenshots_path):
                                self.img_path = str(self.screenshots_path).replace('\\', '/')
                            self._log(self.reason)
                            self._assert_eq()
                    else:
                        if self.reason is not None:
                            try:
                                raise AssertParams(self.error_path, 'self.first', 'self.second', 'self.error')
                            finally:
                                self._log(traceback.format_exc())
                        elif not self.first:
                            self.status = '失败'
                            first = self._strConversion(str(self.first))
                            second = self._strConversion(str(self.second))
                            self.reason = '"%s" 不等于 "%s"' % (first, second)
                            if os.path.exists(self.screenshots_path):
                                self.img_path = str(self.screenshots_path).replace('\\', '/')
                            self._log(self.reason)
                        self._assert_eq()
                else:
                    try:
                        raise AssertParams(self.error_path, 'self.first', 'self.second', 'self.error')
                    finally:
                        self._log(traceback.format_exc())
        finally:
            self._insert_sql(self.status, self.img_path, self.reason)

    def assert_not_eq(self):
        """判断first与second值是不能相等"""
        try:
            if self.first and self.second is not None:
                if isinstance(self.first, type(self.second)):
                    if not self.first == self.second:
                        self.status = '成功'
                        self.reason = self._strConversion(str(self.first))
                        self._assert_not_eq()
                    elif self.first == self.second:
                        self.status = '失败'
                        first = self._strConversion(str(self.first))
                        second = self._strConversion(str(self.second))
                        self.reason = '"%s" 等于 "%s"' % (first, second)
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        self._assert_not_eq()
                else:
                    if not str(self.first) == str(self.second):
                        self.status = '成功'
                        self.reason = self._strConversion(str(self.first))
                        self._assert_not_eq()
                    elif str(self.first) == str(self.second):
                        self.status = '失败'
                        first = self._strConversion(str(self.first))
                        second = self._strConversion(str(self.second))
                        self.reason = '"%s" 等于 "%s"' % (first, second)
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        self._assert_not_eq()
                    elif self.reason is not None:
                        self.status = '错误'
                        reason = self._strConversion(str(self.reason))
                        self.reason = reason
                        if os.path.exists(self.screenshots_path):
                            self.img_path = str(self.screenshots_path).replace('\\', '/')
                        self._log(self.reason)
                        try:
                            raise BaseException(self.reason)
                        finally:
                            self._log(self.reason)
            else:
                if self.reason is not None:
                    self.status = '错误'
                    self.reason = self._strConversion(str(self.reason))
                    if os.path.exists(self.screenshots_path):
                        self.img_path = str(self.screenshots_path).replace('\\', '/')
                    self._log(self.reason)
                    try:
                        raise BaseException(self.reason)
                    finally:
                        self._log(self.reason)
                if isinstance(self.first, type(self.second)):
                    if isinstance(self.first and self.second, bool):
                        if not self.first == self.second:
                            self.status = '成功'
                            self.reason = self._strConversion(str(self.first))
                            self._assert_not_eq()
                        elif self.first == self.second:
                            self.status = '失败'
                            first = self._strConversion(str(self.first))
                            second = self._strConversion(str(self.second))
                            self.reason = '"%s" 等于 "%s"' % (first, second)
                            if os.path.exists(self.screenshots_path):
                                self.img_path = str(self.screenshots_path).replace('\\', '/')
                            self._log(self.reason)
                            self._assert_not_eq()
                    else:
                        if self.reason is not None:
                            try:
                                raise AssertParams(self.error_path, 'self.first', 'self.second', 'self.error')
                            finally:
                                self._log(traceback.format_exc())
                        elif not self.first:
                            self.status = '失败'
                            first = self._strConversion(str(self.first))
                            second = self._strConversion(str(self.second))
                            self.reason = '"%s" 等于 "%s"' % (first, second)
                            if os.path.exists(self.screenshots_path):
                                self.img_path = str(self.screenshots_path).replace('\\', '/')
                            self._log(self.reason)
                        self._assert_not_eq()
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
                             status, self.url, insert_time, img_path, reason, self.author,
                             results_value=self.second)

    @staticmethod
    def _strConversion(values: str):
        """字符串中包含单引号转义成``"""
        res = re.sub("'", "`", values)
        return res.replace("\\", "/")

    def _log(self, reason):
        """记录日志"""
        self.log.logging_debug('执行时间:{},错误路径:{},错误原因:{}'.
                               format(standard_time(), self.error_path, reason))

    def _assert_eq(self):
        """断言相等"""
        self.myself.assertEqual(self.first, self.second, msg=self.reason)

    def _assert_not_eq(self):
        """断言不相等"""
        self.myself.assertNotEqual(self.first, self.second, msg=self.reason)
