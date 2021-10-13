#while, for, do~while(x)
a = 1
while a<=5:
    if a==3:
        break
    print("a=", a)
    a += 1
else:
    print("반복문 정상탈출")
print("반복문 강제탈출 ")

n = 0
while n<5:
    n += 1
    if n == 3:
        continue
    print("n=", n)
