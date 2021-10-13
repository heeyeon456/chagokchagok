import csv

fp = open('data/births.txt')
rd = csv.reader(fp)
data = []
for y, m, f in rd:
    data.append( (int(y), int(m), int(f)) )
print(data)
# 1. 남아 수의 총합을 구하시요.
print( sum([n[1] for n in data]) )

# 2. 남아가 가장 많이 태어난 연도와 남아수를 구하시요.
print( max(data, key=lambda v: v[1]))

# 3. 2000년도 이후에 채어난 대에터를 구하시요
f = filter(lambda v: v[0] >= 2000, data) # generator
for n in f:
    print(n)
