# 총신 octet (8bit byte
# python -- write(send) ---> 장치, 호스트
# str -> bytes 로 변환
# python <------- read(receive) ------ 장치, 호스트
# bytes ---> str로 변환
s = 'abc'
b = b'abc'
print(b)
print( type(b) )
b = b.decode()
print(b)
print( type(b) )
print('========')
s1 = 'korea'
s1 = s1.encode()
print( s1 )
print(type(s1))
