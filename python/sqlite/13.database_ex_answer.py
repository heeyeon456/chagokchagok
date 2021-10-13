import sqlite3
def create_table():
    try:
        sql = 'create table if not exists ' \
              'grade(name varchar(20), korean int, english int, math int)'
        conn = sqlite3.connect('grade.db')
        conn.execute(sql)
        conn.close()
        print('테이블 생성 성공')
    except Exception as err:
        print('테이블 생성 실패')
def insert_grade(name, korean, english, math):
    try:
        sql ="insert into grade values(?, ?, ?, ?)"
        conn = sqlite3.connect('grade.db')
        conn.execute(sql, (name, korean, english, math))
        conn.commit()
        conn.close()
    except Exception as err:
        print('테이블 추가 실패')
def select_grade():
    try:
        sql = "select * from grade"
        db = sqlite3.connect('grade.db')
        cur = db.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        db.close()
        return data
    except Exception as err:
        print(err)
        return None

def inputData():
    while True:
        name = input('이름:')
        korean = int(input('국어:'))
        english = int(input('영어:'))
        math = int(input('수학:'))
        insert_grade(name,korean,english,math)
        if input('계속 입력하시겠습니까(y/n)?') == 'n':
            break
def title():
    print('='*30)
    print('이름', '국어', '영어', '수학', sep='\t')
    print('='*30)

def print_grade():
    for n,k,e,m in select_grade():
        print(n,k,e,m)
create_table()
inputData()
print_grade()
