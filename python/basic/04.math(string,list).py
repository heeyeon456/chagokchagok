# 반지름을 입력받아 원의 면적을 구하시요
#r = input("반지름을 입력하세요: ")
#r = float(r)
#width = 3.14*(r**2)
#print("반지름이 %.f 인 원의 면적은: %.3f" % (r, width))

# 산술연산자 (정수, 실수, bool)
# 문자열 (+, *, %)
# 리스트 (+, *)
#rst = False+3
#print(rst)
s = 'abc'
s = s + 'def'
print(s)
s1 = 'abc'
s1 = s1*3
print(s1)

a = 10
b = 3.14
c = 'korea'
s2 = 'a=%d b=%.2f c=%s' %(a,b,c)
# c언어의 sprintf
print(s2)
s3 = f'a={a:5} b={b} c={c}'
#{a:5} 자리수 5
print(s3)

# 리스트
my = [10, 20, 30]
my = my + [40, 50]
print(my)
my1 = [11,22]
my1 = my1*3
print(my1)
