#tuple
#순서잇는 데이터 타입, immutable
# 반복문 함수에서 많이 사용
# 로직상 이 데이터가 변경되면 안되는 경우
t = (10, 20, 30, 40, 50)
print(t)
print(type(t))
print(t[0])
print(t[1:4])
#t[10] = 100 # 변경불가능

# packing / unpacking
#a = 10; b = 20; c = 30
a, b, c = 10, 20, 30
print(a,b,c)

t1 = 11, 22, 33 # 자동으로 튜플로 변환 -> packing
print(t1)
d,e,f = (1,2,3) # unpaking
print(d,e,f)


