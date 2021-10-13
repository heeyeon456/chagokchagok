class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setName(self,name):
        self.name = name

class Student(People):
    def __init__(self, name, age, stdNum):
        super().__init__(name,age) # 상위클래스 초기화함수 호출
        self.stdNum = stdNum


std = Student(name='홍길동',
              age=20,
              stdNum='20190303')
print(std.name, std.age, std.stdNum)
std.setName('홍길동1')

