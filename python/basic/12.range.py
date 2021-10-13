# python 내장함수
# range(시작값, 끝값, 증가치) 연속된 값의 리스트생성
# 시작값 <= 리스트 < 끝값
r = range( 1, 5, 1)
print(list(r))  # generator

for n in range(1, 6):
    print(n)
