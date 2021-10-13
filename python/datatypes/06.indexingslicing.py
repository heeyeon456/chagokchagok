s='abcdef'
#  012345
#  ...-3-2-1
#인덱싱
print( s[0])
print( s[5])
print( s[-1])
print(s[-3])
# 슬라이싱 [시작인덱스:끝인덱스:증가치]
# 시작인덱스<= index < 끝인덱스
print( s[1:4:1]) #1<=index<4 1,2,3
# bcd
print( s[1:4:2]) #1<=index<4 1,3
# bd
print( s[1:4]) #1<=index<4 1,2,3
# bcd
print( s[:4]) #0<=index<4 0,1,2,3
# abcd
print( s[2:]) #2<=index
# cdef
print( s[:-1]) # 0<= index <-1(5)
#abced
print( s[-1:-5:-1]) #-1<= index<-5
#fedc
print( s[::-1])
# fedcba
