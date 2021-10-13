# 정규식 : 문자열 파싱 (문자열 데이터분석, 인공지능, 웹크롤링)
# [ 매칭 메타 문자 ]
# [메타 문자] [의미]
# . 줄바꿈 문자를 제외한 모든 문자와 매치됨
# ^ 문자열의 시작과 매치됨
# $ 문자열의 마지막과 매치됨
# [ ] 문자 집합 중 한 문자를 의미
# | 또는(or)를 의미
# ( ) 정규식을 그룹으로 묶음

import re

s1 = 'apple kiwi banana'
try:
    # match = re.search('ki.i', s1) # ki 와 i 사이의 한개의 문자가 개행이 아니면 찾아준다.
    # match = re.search('ki\.i', s1) # escape 문자, ki.i 를 찾아줌
    # match = re.search('^app', s1) # app로 시작하는 거
    match = re.search('na$', s1) # ki 와 i 사이의 한개의 문자가 개행이 아니면 찾아준다.
    print(match)
    print( match.group() )
    print( match.span())
except Exception as err:
    print("Not Found")
