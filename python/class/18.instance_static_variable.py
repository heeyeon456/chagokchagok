# 단순한 연산, 처리 (static)
class Circle:
    @staticmethod
    def circleArea(r):
        return r**2*3.14

    @staticmethod
    def cylinder(r, h):
        return r**2*3.14*h

class Student:
    def __init__(self,
                 name :str,
                 age :int):
        self.name = name
        self.age = age
    def show(self):
        print(self.name, self.age)

print(Circle.circleArea(3))
std1 = Student(name='홍길동',
               age=20)
std2 = Student(name='이순신',
               age=30)
std1.show()
std2.show()

data = []
# heap 메모리에 Student 객체가 만들어지고,
# 그에 대한 주소가 data list 에 append 해서 들어감
data.append(
    Student(name='홍길동',
            age=20))
data.append(
    Student(name='이순신',
            age=30))
for s in data: # s는 각 객체의 주소를 가리키게 됨
    s.show()
