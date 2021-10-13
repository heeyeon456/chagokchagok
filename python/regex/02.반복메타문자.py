# [ 반복 메타 문자 ]
# [메타 문자] [의미]
# * 0회 이상 반복
# + 1회 이상 반복
# ? 0회 or 1회
# {m} m회 반복
# {m, n} m회부터 n회까지 반복
import re

s1 = 'apple kiwi banana'
try:
    #match = re.search('ap*le', s1) # p가 0회이상 반복
    #match = re.search('ap+le', s1) # p가 1회이상 반복
    #match = re.search('ap?le', s1) # p가 0 또는 1회 반복
    #match = re.search('ap{2}le', s1) # p가 m회 반복
    match = re.search('ap{2, 4}le', s1) # p가 m <=p<= n
    print(match)
    print( match.group() )
    print( match.span())
except Exception as err:
    print("Not Found")
