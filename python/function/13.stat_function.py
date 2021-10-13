data1 = [10, 20, 30, 25]
data2 = [(10, 20), (70,15), (40,50)]
data3 = [{'kor':10, 'eng':20},
         {'kor':70, 'eng':15},
         {'kor':40, 'eng':50}]
mx = max(data1)
print(mx)
mx = max(data2, key=lambda v: v[0])
print(mx)

f = filter(lambda v:v>=20, data1)
print(list(f))

def myfilter(func, dt):
    return (n for n in dt if func(n)) # generator

f = myfilter(lambda v:v>=20, data1)
print(list(f))

# 정렬된 리스트 반환
s = sorted(data1)
print(s)
s = sorted(data2, key=lambda v:v[0])
print(s)

print(sum(data1))

m = map( lambda v:v+2, data1)
print( list(m))
