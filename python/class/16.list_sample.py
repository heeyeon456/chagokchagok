"""
# list 클래스 객체 생성
# my = list([10, 20, 30, 40])
my = [10, 20, 30, 40]
my1 = my # shallow copy # 주소값만 복사
print(id(my1), id(my))
print('----------------')
#my1 = [10, 20, 30, 40 ]
my1 = my.copy() # deep copy # 값도 복사 (heap 영역에 새로운 메모리를 할당하는 것
my1[0] = 100
print(id(my1), id(my))
print(my)
print(my1)
"""

# my를 heap 에 핼당
# aa는 지역변수에 할당, my를 shallow copy
# my의 주소값을 받아서 값 변경, aa는 스택에서 해제
my = [10, 20, 30, 40 ]
def fn(aa):
    aa[0] = 100

fn(my)  ## my 리스트의 값 변경 (100으로)
print(my)
