g = 10
def fn():
    g = 100
    print(locals())
# 지역변수는 함수호출이 끝나면 소멸되기 때문에 함수안에서 지역변수를 확앤해야함
fn()
print("g=", g)
print( globals() ) # python complier 가 만들어주는 전역변수들
print(__file__)
# python 은 runtime binding : 함수의 시작주소를 호출하고 실행

