import os
from model.SQL import Mysql

class MyAssert:
    def __init__(self,driver,first,second,case_count,case_error,case_name,case_remark,case_time,url):
        """初始化"""
        self.driver = driver
        self.first = first
        self.second = second
        self.case_count = case_count
        self.case_error = case_error
        self.case_name = case_name
        self.case_remark = case_remark
        self.case_time = case_time
        self.case_url = url
        self.DB = Mysql()
        img = os.path.dirname(os.path.dirname(__file__))
        self.img_path = os.path.join(img + '/img', '{}.png'.format(self.case_name))

    def start_assert(self):
        """执行断言判断"""
        try:
            self.driver.assertEqual(self.first,self.second)
            self.status = '成功'
        except:
            self.status = '失败'
            self.img = self._img_exist()
        else:
            if self.case_error is not None:
                self.status = '错误'
                self.img = self._img_exist()
        finally:
            self.DB.insert_data(self.case_count,self.case_name,self.case_remark,
                                self.case_time,self.status,self.case_url,self.img,
                                self.case_error,)

    def _img_exist(self):
        """检查截图的图像是否存在"""
        self.driver.save_screenshot(self.img_path)
        if self.img_path:
            img = self.img_path.replace('\\','/')
            return str(img)
