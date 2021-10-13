# 함수기반설계원칙( Clean Code )
# 결합도 ,if 문, 명명규칙
# 1. SRP  단일책임(Single Responsible Priciple)
# 하나의 함수에서는 하나의 기능만 해야 한다..
# 2. Open-Closed (함수포인터)
# 함수안에서 변동가능가능한 부분을 함수주소를
# 이용해서 분리시키는것

data1 = [10, 20, 30, 25]
data2 = [(10, 20), (70,15), (40,50)]
data3 = [{'kor':10, 'eng':20},
         {'kor':70, 'eng':15},
         {'kor':40, 'eng':50}]

# 데이터 타입에 따라 복잡해짐
def mymax(dt):
    mx = dt[0]
    for n in dt[1:]:
         if n['kor'] > mx['kor']: mx = n
         #if n[0] > mx[0]: mx = n
         #if n > mx: mx = n
    return mx

# 함수형태 하나로 해결
# 되게 함수가 무한정 늘어남
# 프로그램 종료 전까지 메모리에 고정적으로 잡고 있음
# -> 이 목적에 의해서 임시로 사용하고 사라질 수 있는 함수의 필요성 --> 람다함수
def fn1(v):
    return v

def fn2(v):
    return v[0]

def fn3(v):
    return v['kor']

def mymax2(dt, key):
    mx = dt[0]
    for n in dt[1:]:
        if key(n) > key(mx) :
            mx = n
    return mx
#mx = mymax(data3)
#print(mx)
m = mymax2(data3, fn3)
print(m)
