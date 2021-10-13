import sqlite3

class StudentScore:
    def __init__(self, dbname, table_name):
        self.dbname = dbname
        self.tablename = table_name
        self.num_of_stu = 0

    @classmethod
    def defaultFn(cls):
        print("1, 2, 3, 4 번 중 하나의 숫자를 입력하세요")

    def getMenu(self):
        print("메인 메뉴)\n\t1. 입력\n\t2. 출력\n\t3. 종료")
        try:
            number = int(input("번호를 입력하세요: "))
            menu = {1:self.getInput,
                    2:self.printOut,
                    3:self.exit}
            menu.get(number, self.defaultFn)()
        except:
            print("숫자를 입력하세요")

    def _createTable(self):
        try:
            conn = sqlite3.connect(self.dbname)
            sql = 'create table if not exists {}(name var(20), ' \
                        'korean int, english int, math int, total int, avg float)'.format(self.tablename)
            conn.execute(sql)
            print("테이블 생성 성공")
        except Exception as err:
            print(err)
            conn.close()
        return conn

    def _insertTable(self, conn, data):
        command = f"insert into {self.tablename} values(?,?,?,?,?,?)"
        try :
            conn.execute(command, data)
            conn.commit()
        except Exception as err:
            print(err)

    def _selectTable(self):
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

    def getInput(self):
        # 1. 입력
        conn = self._createTable()

        isContinue = True
        while isContinue:
            name = input("이름: ")
            korean = int(input("국어: "))
            english = int(input("영어: "))
            math = int(input("수학: "))
            sum = korean + english + math
            data = (name, korean, english, math, sum, round(sum / 3, 2))
            self._insertInput(conn, data)
            while 1:
                tmp = input("게속 입력하시겠습니까?(y/n) ")
                print(tmp)
                if tmp == 'n' or tmp == 'y': break
                print("y, n 중 하나의 정답을 입력흐세요. ")
            isContinue = True if tmp == 'y' else False

        conn.close()
        self.getMenu()

    def _title(self):
        print("-"*30)
        print("이름\t국어\t영어\t수학\t총점\t평균")
        print("-"*30)

    def printOut(self):
        # 2. 출력
        total_score_list = []
        self._title()

        dt = self._selectTable()
        for s in dt:
            for k in s:
                print("{}".format(k), end='\t')
            print()
        print("-"*30)


    def __del__(self):
        pass

    def exit(self):
        # 4. 종료
        self.__del__()

if __name__ == "__main__":
    obj = StudentScore("score.db", "grade")
    obj.getMenu()
