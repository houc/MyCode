import os

from model.SQL import Mysql


class MyAsserts():
    def __init__(self,first,second,id,level,name,remark,status,reason,url,time,other,driver,screenshots_path):
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
        self.img_path = None
        self.sql = Mysql()

    def asserts(self):
        """判断first与second值是否相等"""
        if self.first and self.second is not None:
            if self.first == self.second:
                self.status = '成功'
            elif not self.first == self.second:
                self.status = '失败'
                self.driver.save_screenshot(self.screenshots_path)
                self.reason = '%s != %s'%(self.first,self.second)
        if self.first is None:
            self.status = '错误'
            self.driver.save_screenshot(self.screenshots_path)
        if os.path.exists(self.screenshots_path):
            self.img_path = self.screenshots_path
        self._insert_sql(self.status,self.img_path,self.reason)

    def _insert_sql(self,status,img_path,reason):
        """将用例插入数据库"""
        print(reason)
        self.sql.insert_data(self.id,self.level,self.name,self.remark,"%.3fs"%self.time,status,
                             self.url,img_path,reason,self.other)

if __name__ == '__main__':
    MyAsserts(None,'','','','','','','','','','','','',).asserts()