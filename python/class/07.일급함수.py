# 일급함수 (first class fucntion)
# 할당, 리턴, 인자, 함수안에 함수정의 (decorator)

def fn():
    print('fn call')

def afn( aa):
    aa()

def rfn():
    return fn

rst = rfn()
rst()

#my = fn # 함수의 주소값이 복사됨
#print(id(fn), id(my))
#my()

#afn( fn ) // argument의 주소값으로 이동해서 fn이 호ㄹ출되게 됨

