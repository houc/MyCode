import sqlite3
import queue

from config_path.path_file import read_file
from model.Yaml import MyConfig


class MyDB(object):
    def __init__(self, switch=False):
        self.sql = self._connect_sql()
        self.queue = queue.Queue()
        self.dbTable = MyConfig('sql_table').sql
        self.dbTitle = MyConfig('sql_create_title').sql
        self.dbQuery = MyConfig('sql_query').sql
        self.dbDelete = MyConfig('sql_delete').sql
        self.dbInsert = MyConfig('sql_insert').sql
        self.update = MyConfig('sql_update').sql
        if switch:
            self._insert_title()

    def _connect_sql(self):
        db_path = read_file('package', 'DB.db')
        conn = sqlite3.connect(db_path, timeout=360, check_same_thread=False)
        return conn

    def _insert_title(self):
        DB = self.sql.cursor()
        DB.execute(self.dbTable)
        DB.execute(self.dbTitle)

    def query_data(self):
        save_data = []
        DB = self.sql.cursor()
        DB.execute(self.dbQuery)
        data = DB.fetchall()
        for a in data:
            save_data.append(list(a))
        return save_data

    def delete_data(self):
        DB = self.sql.cursor()
        DB.execute(self.dbDelete)
        self.sql.commit()

    def insert_data(self, case_catalog=None, case_level=None, case_module=None,
                    case_name=None, case_url=None, case_scene=None, case_status=None,
                    case_results=None, case_error_reason=None, case_insert_parameter=None,
                    case_wait_time=None, case_img=None, case_author=None, case_remark=None,
                    insert_time=None):

        data = self.dbInsert % (case_catalog, case_level, case_module, case_name,
                                case_url, case_scene, case_status, case_results,
                                case_error_reason, case_insert_parameter, case_wait_time, case_img,
                                case_author, case_remark, insert_time)
        DB = self.sql.cursor()
        self.queue.put(data)
        while not self.queue.empty():
            data = self.queue.get()
            DB.execute(data)
            self.sql.commit()
            self.close_sql()

    def close_sql(self):
        return self.sql.close()

    def update_db(self, row_name_value, sign_action):
        update = self.update % (row_name_value, sign_action)
        DB = self.sql.cursor()
        DB.execute(update)
        self.sql.commit()


if __name__ == '__main__':
    query = MyDB().query_data()
    print(query)
    # up = MyDB().update_db(row_name_value='case_catalog="你好"', sign_action='case_name="test_error"')
