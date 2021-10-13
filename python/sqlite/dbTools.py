import sqlite3
class DBTools:
    def __init__(self, dbname, table_name):
        self.dbname = dbname
        self.tablename = table_name

    def createTable(self):
        try:
            conn = sqlite3.connect(self.dbname)
            sql = 'create table if not exists {}(name var(20), ' \
                        'count int)'.format(self.tablename)
            conn.execute(sql)
            print("테이블 생성 성공")
        except Exception as err:
            print(err)
            conn.close()
        return conn

    def insertTable(self, data):
        command = f"insert into {self.tablename} values(?,?)"
        try :
            conn = sqlite3.connect(self.dbname)
            conn.execute(command, data)
            conn.commit()
        except Exception as err:
            print(err)

    def selectTable(self):
        sql = f"select * from {self.tablename}"
        try:
            conn = sqlite3.connect(self.dbname)
            cur = conn.cursor()
            cur.execute(sql)
            dt = cur.fetchall()
        except Exception as err:
            print(err)
        conn.close()
        return dt
