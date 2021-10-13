# 정규식 : 문자열 파싱 (문자열 데이터분석, 인공지능, 웹크롤링)
# regular expression
import re

s1 = 'apple kiwi banana'
try:
    match = re.search('melon', s1)
    print(match)
    print( match.group() )
    print( match.span())
except Exception as err:
    print("Not Found")

