n = '22'
n = int(n)
print(n, type(n))

a = 10
a = str(a)
print(a, type(a))

b = '3.12'
b = float(b)
print(b, type(b))
print("-----------")

c = (10, 20, 30)
c = list(c)
print(c, type(c))

d = [10, 20, 30]
d = tuple(d)
print(c, type(c))
print("-----------")

e = {'aa':10, 'bb':20}
e = list(e)
print(e, type(e))

f = [10, 20, 30]
f = enumerate(f)  ### enumeratoe 객체로 변환
f = dict(f) # 인덱스가 Key 가 되어 dictionary 로 변환
print(f, type(f))
print("-----------")

aa = ['a','b','c']
bb = [1,2,3]
z = zip(aa, bb)
print(z) # generator
print(dict(z))



