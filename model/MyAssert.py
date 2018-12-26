import os
import re
import time

from model.SQL import Mysql


class MyAsserts():
    def __init__(self, first, second, id, level, name, remark, status, reason, url, time,
                 other, driver, screenshots_path, author):
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
        self.other = other
        self.driver = driver
        self.screenshots_path = screenshots_path
        self.author = author
        self.img_path = None
        self.sql = Mysql()

    def asserts(self):
        """判断first与second值是否相等"""
        if self.first and self.second is not None:
            if type(self.first) is type(self.second):
                if self.first == self.second:
                    self.status = '成功'
                elif not self.first == self.second:
                    self.status = '失败'
                    self.driver.save_screenshot(self.screenshots_path)
                    first = self._strConversion(str(self.first))
                    second = self._strConversion(str(self.second))
                    self.reason = '%s != %s' % (first, second)
                    if os.path.exists(self.screenshots_path):
                        self.img_path = str(self.screenshots_path).replace('\\', '/')
            else:
                if str(self.first) == str(self.second):
                    self.status = '成功'
                elif not str(self.first) == str(self.second):
                    self.status = '失败'
                    self.driver.save_screenshot(self.screenshots_path)
                    first = self._strConversion(str(self.first))
                    second = self._strConversion(str(self.second))
                    self.reason = '%s != %s' % (first, second)
                    if os.path.exists(self.screenshots_path):
                        self.img_path = str(self.screenshots_path).replace('\\', '/')
        else:
            if self.reason is not None:
                self.status = '错误'
                self.driver.save_screenshot(self.screenshots_path)
                reason = self._strConversion(str(self.reason))
                self.reason = reason
            if os.path.exists(self.screenshots_path):
                self.img_path = str(self.screenshots_path).replace('\\', '/')
        self._insert_sql(self.status, self.img_path, self.reason)

    def _insert_sql(self, status, img_path, reason):
        """将用例插入数据库"""
        insert_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.sql.insert_data(self.id, self.level, self.name, self.remark, "{:.4f}s".format(self.time), status,
                             self.url, insert_time, img_path, reason, self.author, self.other)

    def _strConversion(self,values):
        """字符串中包含单引号转义成``"""
        if isinstance(values, str):
            res = re.sub("'", '`', values)
            return res
        else:
            raise TypeError(values)


if __name__ == '__main__':
    T = MyAsserts(None,'','','','','','','','','','','','','')
    print(T)