import re
s1 = 'apple kiRi banana'
s2 = '서울시 은평구'
try:
    # match = re.search('ki[vwx]i', s1) # 대괄호안의 하나의 문자안에 속하면 찾아줌
    # match = re.search('ki[a-z]i', s1) # 소문자중 하나면 찾아줌
    # match = re.search('ki[vwx]+i', s1) # v/w/x 중 하나가 1회이상 반복
    # match = re.search('ki[a-zA-Z]+i', s1) # 영어 소문자, 대문자 중 하나가 1회이상 반복
    # match = re.search('ki[a-zA-Z0-9_#]+i', s1) # 영어 소문자, 대문자, 숫자, # 하나가 1회이상 반복
    # match = re.search('ki[^a-z]+i', s1) # 대괄호안 ^ : not
    # match = re.search('ki[^a-z]+i', s1)
    # match = re.search('ki[^a-z]+i', s1)
    # match = re.search('서울[시군구]', s2) #
    match = re.search('서울[가-힣]', s2) # 한글만
    print(match.group())
except Exception as err:
    print('not found')
