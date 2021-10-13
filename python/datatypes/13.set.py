# 중복 데이터 제거
# 집합 연산자 (&(합), -(차), |(교), ^(대상차) )
s = {10,20,30,40,50,20,20,30}
print(s)
print( type(s) )
# print(s[0]) # error
s.add(100) # 중간추가x, element
s.add(200)
s.remove(20)
print(s)
print( type(s) )

# 집합 연산자 사용가능
s1 = {10,20,30}
s2 = {20,30,40,50}
print( s1&s2 ) #교집합
print( s1|s2 ) # 합집합
print( s1-s2 ) # 차집합
print( s1^s2 ) # 대상차집합

