import sqlite3
import queue

from config_path.path_file import read_file
from model.Yaml import MyConfig


class MyDB(object):
    def __init__(self, switch=False):
        """
        数据库（用于db）
        :param switch:
        """
        self.sql = self._connect_sql()
        self.queue = queue.Queue()
        self.dbTable = MyConfig('sql_table').sql
        self.dbTitle = MyConfig('sql_create_title').sql
        self.dbQuery = MyConfig('sql_query').sql
        self.dbDelete = MyConfig('sql_delete').sql
        self.dbInsert = MyConfig('sql_insert').sql
        if switch:
            self._insert_title()

    def _connect_sql(self):
        """连接数据库"""
        db_path = read_file('package', 'DB.db')
        conn = sqlite3.connect(db_path, timeout=360, check_same_thread=False)
        return conn

    def _insert_title(self):
        """检查数据库表头，并创建数据库表头"""
        DB = self.sql.cursor()
        DB.execute(self.dbTable)
        DB.execute(self.dbTitle)

    def query_data(self):
        """查询数据库全部的信息"""
        save_data = []
        DB = self.sql.cursor()
        DB.execute(self.dbQuery)
        data = DB.fetchall()
        for a in data:
            save_data.append(list(a))
        return save_data

    def delete_data(self):
        """清除所有数据"""
        DB = self.sql.cursor()
        DB.execute(self.dbDelete)
        self.sql.commit()

    def insert_data(self, id, level, module, name, remark, wait_time, status, url, insert_time, img=None,
                    error_reason=None, author=None, *, results_value):
        """插入数据"""
        if error_reason:
            if len(error_reason) < 10000:
                error_reason = error_reason[:10000]
        data = self.dbInsert % (id, level, module, name, url, remark, status, results_value, error_reason, wait_time,
                                img, author, insert_time)

        DB = self.sql.cursor()
        self.queue.put(data)
        while not self.queue.empty():
            data = self.queue.get()
            DB.execute(data)
            self.sql.commit()
            self.close_sql()

    def close_sql(self):
        """关闭数据库"""
        return self.sql.close()

if __name__ == '__main__':
    query = MyDB(True).query_data()
    print(query)
