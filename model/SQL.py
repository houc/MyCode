from pymysql.connections import Connection
from model.Yaml import MyYaml

class Mysql:
    def __init__(self,coding = 'utf8'):
        self.dbHost = MyYaml('address').sql
        self.dbUser = MyYaml('account').sql
        self.dbPsw = MyYaml('password').sql
        self.dbPort = MyYaml('port').sql
        self.dbBase = MyYaml('name_db').sql
        self.decoding = coding
        self.DB = self._connect_sql()

    def _connect_sql(self):
        db = Connection(
            host = self.dbHost,
            user = self.dbUser,
            password = self.dbPsw,
            database = self.dbBase,
            port = self.dbPort,
            charset = self.decoding
        )
        return db.cursor()


