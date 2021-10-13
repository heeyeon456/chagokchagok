import sqlite3 as sql3

# DB가 없으면, 생성후 접송
# DB가 있으면, 접솝
def createTable():
    try:
        conn = sql3.connect('test.db')
        sql_command = 'create table if not exists student(name var(20),' \
            'age int, birth date)'
        conn.execute(sql_command)
        conn.close()
        print("테이블 생성 성공")
    except Exception as err:
        print("테이블 생성 실패")

def insertTable():
    # insert, delete, update 이 세가지 구문은 commit 이 반드시 필요
    try:
        command = "insert into student values('홍길동',20,'1999-10-11')"
        conn = sql3.connect('test.db')
        conn.execute(command)
        conn.commit() # 명령 확정
        conn.close()
        print("테이블 추가 성공")
    except Exception as err:
        print("추가 실패")
        conn.close()

def insertFormat(name, age, birth):
    try:
        command = "insert into student values(?,?,?)"
        conn = sql3.connect('test.db')
        conn.execute(command, (name, age, birth))
        conn.commit() # 명령 확정
        conn.close()
        print("테이블 추가 성공")
    except Exception as err:
        print("추가 실패")
        conn.close()

def insertDataBulk():
    try:
        sql = "insert into student values(?,?,?)"
        conn = sql3.connect('test.db')
        data =[('김철수',30,'1989-10-10'),
               ('이황',40,'1979-12-15'),
               ('이이',50,'1969-03-18')]
        conn.executemany(sql,  data )
        conn.commit()
        conn.close()
        print("insert success")
    except Exception as err:
        print(err)

def updateData():
    try:
        sql="update student set name=?, age=? where name=?"
        db = sql3.connect("test.db")
        db.execute(sql, ('이황황',20, '이황') )
        db.commit()
        db.close()
        print("update data ")
    except Exception as err:
        print(err)

def deleteData():
    try:
        sql="delete from student where name=?"
        db = sql3.connect("test.db")
        db.execute(sql, ('이황황',) )
        db.commit()
        db.close()
        print("delete data ")
    except Exception as err:
        print(err)

def selectData():
    try:
        sql = "select * from student"
        db = sql3.connect("test.db")
        # connection 개체가 아닌 커서 개체로 sql execute
        cur = db.cursor()
        cur.execute(sql)
        dt = cur.fetchall()
        #db.execute(sql)
        db.close()
        print(dt)
        for n,a,b in dt:
            print(n,a,b)
    except Exception as err:
        print(err)

def selectCur():
    try:
        sql="select * from student"
        db = sql3.connect("test.db")
        cur = db.cursor()
        cur.execute(sql)
        for n,a,b in cur:
            print( n,a,b )
        db.close()
    except Exception as err:
        print(err)

def deleteCursor():
    try:
        sql="delete from student where age=?"
        db = sql3.connect("test.db")
        cur = db.cursor()
        cur.execute(sql, (30, ))
        print("삭제 된 갯수", cur.rowcount)
        db.commit()
        db.close()
    except Exception as err:
        print(err)

deleteCursor()
