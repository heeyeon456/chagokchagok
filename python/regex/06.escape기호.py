
# 이스케이프 기호 ]
# [종류] [설명]
# \d 모든 숫자와 매치됨 [0-9]
# \D 숫자가 아닌 문자와 매치됨 [^0-9]
# \s 화이트 스페이스 문자와 매치됨 [ \t\n\r\f\v]
# \S 화이트 스페이스가 아닌 것과 매치됨 [^ \t\n\r\f\v]
# \w 숫자 또는 문자와 매치됨 [a-zA-Z0-9_]
# \W 숫자 또는 문자가 아닌 것과 매치됨 [^a-zA-Z0-9_]
# \b 단어의 경계를 나타냄. 단어는 영문자 혹은 숫자의 연속 문자열
# \B 단어의 경계가 아님을 나타냄
# \A 문자열의 처음에만 일치
# \Z 문자열의 끝에만 일치

import re

s1 = 'apple kiwi banana'
s2 ="123-abc def-ghi 346-Abc"

try:
    # match = re.search('ki\di', s1) # ki[0-9]i
    # match     = re.search('ki\Di', s1) # ki[^0-9]i
    # match = re.search('ki[\diabc]', s1) # ki[0-9]i
    # match = re.search('ki\wi', s1) # ki[a-zA-Z0-9_]i
    match = re.search('(\d{3})-([a-z]{3})', s2)
    print( match.group() )
    print( match.group(1) )
    print( match.group(2) )
    print(match.groups())
except Exception as err:
    print("Not Found")
