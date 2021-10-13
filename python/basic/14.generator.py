import sys

# generator ***중요!!!! ***
# list compresion
my = [n*10 for n in range(1, 4)]
#print(my)
print(sys.getsizeof(my))
# 연산이 더빠름, 메모리 소모가 큼
#for n in my: # n = my[0], n=my[1]
#    print(n)

# tuple 아닌 generator object
# 연산결과를 메모리에 담고있지 않고, 하나씩 하나씩 next를 통해서 처리하는 것
g = (n*10 for n in range(1,4))
print( list(g) ) # [next(g), next(g), next(g) ...]

#print(g)
print(sys.getsizeof(g))
#print(next(g))
#print(next(g))
# 연산이 더느림, 메모리 소모 적음
for n in g: # n=next(g) , n=next(g)
    print(n)



