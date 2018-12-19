import traceback

from pymysql.connections import Connection
from model.Yaml import MyYaml


class Mysql:
    def __init__(self,coding = 'utf8'):
        """初始化"""
        self.dbHost = MyYaml('address').sql
        self.dbUser = MyYaml('account').sql
        self.dbPsw = MyYaml('password').sql
        self.dbPort = MyYaml('port').sql
        self.dbBase = MyYaml('name_db').sql
        self.dbTable = MyYaml('sql_table').sql
        self.dbTitle = MyYaml('sql_create_title').sql
        self.dbQuery = MyYaml('sql_query').sql
        self.dbInsert = MyYaml('sql_insert').sql
        self.dbDelete = MyYaml('sql_delete').sql
        self.dbUpdate = MyYaml('sql_update').sql
        self.decoding = coding
        self.DB = self._connect_sql()
        # self._insert_title()

    def _connect_sql(self):
        """连接数据库"""
        db = Connection(
            host = self.dbHost,
            user = self.dbUser,
            password = self.dbPsw,
            database = self.dbBase,
            port = self.dbPort,
            charset = self.decoding
        )
        return db

    def _insert_title(self):
        """检查数据库表头"""
        DB = self.DB.cursor()
        DB.execute(self.dbTable)
        DB.execute(self.dbTitle)

    def query_data(self):
        """查询数据"""
        save_data = list()
        DB = self.DB.cursor()
        DB.execute(self.dbQuery)
        data = DB.fetchall()
        for a in data:
            save_data.append(list(a))
        return save_data

    def insert_data(self,id,level,name,remark,wait_time,status,url,img=None,error_reason=None,other=None):
        """插入数据"""
        DB = self.DB.cursor()
        data = self.dbInsert%(id,level,name,remark,img,status,url,error_reason,wait_time,other)
        DB.execute(data)
        self.DB.commit()

    def delete_data(self):
        """清除所有数据"""
        DB = self.DB.cursor()
        DB.execute(self.dbDelete)
        self.DB.commit()

    def close_sql(self):
        """关闭数据库"""
        return self.DB.close()

    def update_sql(self,parameter,case_name):
        """更新数据库部分字段"""
        DB = self.DB.cursor()
        data = self.dbUpdate%(parameter,'case_name={0!r}'.format(case_name))
        DB.execute(data)
        self.DB.commit()


if __name__ == '__main__':
    M = Mysql()
    # M.insert_data('1','name','remark','26.555s','失败','/auto_ui/model','d:/','"chengg" ！= "ass sds sdsd !"')
    # M.update_sql("case_status='成功1'",'test_accountAndEnglish')
    print(M.query_data())