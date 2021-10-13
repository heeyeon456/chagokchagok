import sqlite3
def insertMany():
    data = [('김철수',30,'1989-12-15'),
            ('이황',40,'1979-10-10'),
            ('이이',50,'1969-02-16'),
            ('임꺽정',60,'1959-11-10'),
            ('이순신',70,'1949-10-17'),
            ('정난정',10,'2010-12-10'),
            ('김철이',20,'1999-07-23'),
            ('황김순',30,'1989-10-10')
            ]
    try:
        sql = "insert into student values(?,?,?)"
        db = sqlite3.connect("test.db")
        db.executemany(sql, data )
        db.commit()
        db.close()
        print("insert data ")
    except Exception as err:
        print(err)

def selectCur():
    try:
        # sql="select * from student"
        # sql="select * from student where age=40"
        # sql="select * from student where age=40 or age=50"
        # sql="select * from student where age in(20,30,40)"
        # sql="select * from student where age>=20"
        # sql="select * from student where age>=20 and age<=30"
        # sql="select * from student where age between 20 and 40"
        # sql="select * from student where name='김철수'"
        # sql="select * from student where name>='이이'"
        # sql="select * from student where birth>='1980-01-01'"
        # sql="select * from student where name like '%김%'"
        sql="select * from student order by name"
        # sql="select * from student order by age desc"
        # sql="select * from student order by age desc limit 3"
        db = sqlite3.connect("test.db")
        cur = db.cursor()
        cur.execute(sql)
        for n,a,b in cur:
            print( n,a,b )
        db.close()
    except Exception as err:
        print(err)

#insertMany()
selectCur()
