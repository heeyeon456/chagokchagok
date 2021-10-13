data1 = [10, 20, 30, 25]
data2 = [(10, 20), (70,15), (40,50)]
data3 = [{'kor':10, 'eng':20},
         {'kor':70, 'eng':15},
         {'kor':40, 'eng':50}]

def mymax2(dt, key):
    mx = dt[0]
    for n in dt[1:]:
        if key(n) > key(mx) :
            mx = n
    return mx
#mx = mymax(data3)
#print(mx)
# lambda 함수가 지역변수로 호출되기 때문에 함수 호출이 끝나면 지역변수에서 해제됨
# key 인자가 지역변수로 주소를 가지고 있는데, 호출이 끝나면 지역변수가 소멸되고 reference 하고있는게 zero 가 되면서 메모리에서 해제됨
# 목적을 달성하면 소멸
m = mymax2(data1, lambda v:v)
print(m)

m = mymax2(data2, lambda v:v[0])
print(m)
