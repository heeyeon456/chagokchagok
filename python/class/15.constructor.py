class Test:
    def __init__(self, x, y ):
        print("init call")
        self.a = x
        self.b = y
    def __del__(self): #객체소멸직전 자동호출
        print("dest call")
    def setData(self,x,y):
        self.a = x
        self.b = y
    def show(self):
        print(self.a, self.b)

obj = Test(10, 20) # obj.__init__(obj, 10, 20)
my = obj # obj reference count = 2
obj = 1
# 소멸자 바로 호출
# heap 메모리에 class 객체 부분 할당
# obj가 그 메모리 주소 할당
# 근데 obj 가 1이라는 int 를 할당하게 바뀌면 그 메모리의 reference count = 0
# 바로 메모리에서 소멸자 함수 호출
# 파이썬의 메모리 관리방식 (RC: 참조계수기법)
# 주소 복사 shellow copy

obj = Test(10, 20) # obj.__init__(obj, 10, 20)
my = obj # obj reference count = 2
print(id(my), id(obj))
obj = 1 # obj reference count = 1 , 소며차 호출 안됨
my.show()
print(id(my), id(obj))
print('hello')
# 프로그램 종료 시 소멸자 호출

print('------------------')
"""
def fn():
    obj = Test(11,22)  # heap 메모리에 객체를 생성한다음에 stack 영역의 obj변수에 해당 주소값을 저장
    obj.show()
fn()  #함수안에서 obj는 스택 메모리에 할당
# 함수 호출이 끝남 소멸자 호출
"""

def fn():
    obj = Test(11,22)
    obj.show()
    return obj

rst = fn()  #cpu의 리턴값 저장영역에 저장
# 임시저장된 imsi 변수의 값을 rst에게 줌
rst.show() # rst.show(rst) #self
print('hello')
# 프로그램이 끝날 때 소멸자 호출
