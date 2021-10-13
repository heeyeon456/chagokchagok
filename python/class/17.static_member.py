class Test:
    st = 10 # static 변수 : 함수 몸체 밖에 선언된 변수 (객체 생성과는 무관)
    # python 이 바로 메모리의 global 영역에 st를 올려버림
    def __init__(self):  #생성자 함수 : 객체 생성시 자동 호출
        print("init call")
        # 객체가 생성되야 메모리에 올라감
        self.a = 0 #인스턴스 변수(객체 생성지 할당)
        self.b = 0
    def __del__(self): #객체소멸직전 자동호출
        print("dest call")
    def setData(self,
                x :int,
                y :int):
        self.a = x
        self.b = y
    def show(self):
        print(self.a, self.b)

    @staticmethod  # decorator (오동작 할 수 있음)
    def stFn(a: int): # self 없이 정의
        # static method (정적 멤버함수)
        # 인스턴스 변수는 사용 불가
        Test.st  = a
        print('stfn call')

    @classmethod #decorator
    def clsFn(cls,
              a :int):
        cls.st = a # Test.st = a 와 같은 의미
        print('cls fn call')

Test.stFn(11) # 객체를 넘겨줄수가 없음 (self가 없음)
print(Test.st) # 객체 생성과 무관한 공유변수 (static 변수)
Test.clsFn(12) # static method 와 같은 개념인데,
# 파이썬 컴파일러가 Test.clsFn(Test,12) 이렇게 바꿔줌
print(Test.st)

# obj = Test()
# obj.setData(10,20) # 반드시 객체를 생성하고 호출해야함
# obj.stFn() # python compiler 가 obj.stFn(obj)처럼 오동작 할 수 있음
# 모든 클래스는 object 라는 클래스를 상속받음
