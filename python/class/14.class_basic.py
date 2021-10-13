class Test:
    # 생성자 함수
    def __init__(self):
        print("init call")
        self.a = 10
        self.b = 20
    def setData(self, x, y):
        print('setData self 주소', id(self))
        self.a = x
        self.b = y
    def show(self):
        print('show self 주소', id(self))
        print(self.a, self.b)

# heap 메모리에 a,b 변수를 올려주고, obj 가 할당된 메모리의 시작주소를 반환한다.
# obj 주소값 자체는 global 변수로 저장한다.
obj = Test() # 다른 언어 new Test()
# obj.__init__(obj)
print('obj 주소', id(obj))

obj.setData(100, 200) # obj.setData(obj,100,200) 파이썬 컴파일러가 이렇게 조정
obj.show() # obj.show(obj)
print()

obj1 = Test()
print('obj1 주소', id(obj1))
obj1.setData(11,22)
obj1.show()

# 동일한 클래스에서 여러개의 객체가 발생할 경우,
#멤qj 데이터는 메모리 별도로 (heap)
# 멤버 함수(코드)는 공유
# 어떻게 각각의 멤버데이터 영역에  r/w self

