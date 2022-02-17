from sqlalchemy import create_engine

class Connection():
    def __init__(self, hostname=None, database=None):
        self.hostname=hostname
        self.database=database
        self.enigne = None

    def get_engine(self):
        return self.enigne

class OracleConnection(Connection):

    def oracle_authentication(self, hostname=None, port=None, database=None, username=None, password=None):
        super().__init__(hostname, database)
        self.enigne = create_engine(fr"oracle+cx_oracle://{username}:{password}@{self.hostname}:{port}/{self.database}?encoding=UTF-8&nencoding=UTF-8")

class SQLServerConnection(Connection):

    def windows_authentication(self, hostname, database):
        super(SQLServerConnection, self).__init__(hostname, database)
        self.enigne = create_engine(fr'mssql+pyodbc://@{self.hostname}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server', fast_executemany=True)

    def sql_server_authentication(self, hostname=None, port=None, database=None, username=None, password=None):
        super(SQLServerConnection, self).__init__(hostname, database)
        self.enigne = create_engine(fr"mssql+pyodbc://{username}:{password}@{self.hostname}:{port}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server", fast_executemany=True)

class MySQLConnection(Connection):

    def mysql_authentication(self, username, password, hostname, port,database):
        super(MySQLConnection, self).__init__(hostname, database)
        self.enigne  = create_engine(fr'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}')