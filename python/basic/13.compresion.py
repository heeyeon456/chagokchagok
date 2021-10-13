my = [n*10 for n in range(1,6)]
print(my)

my1 = [n*10 for n in range(1,6) if n>=3]
print(my1)

# 각 연봉의 세금 3.3 % 를 제한 실수령액 리스트를 구하시요
salary = [1000, 2000, 3000, 4000, 5000]
real_s = [int(x-x*0.033) for x in salary]
print(real_s)
print("----------------")

my2 = {n*10 for n in range(1,6)} # set 이 됨
print(my2)
