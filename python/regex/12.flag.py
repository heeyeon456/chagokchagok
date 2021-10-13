# rs.search의 flag argument
# I, IGNORECAT E 대, 소문자를 구별하지 않는다
# L, LOCAT E \w, \W, \b, \B를 현재의 로케일에 영향을 받게 한다
# M , M ULT ILINE ^가 문자열의 맨 처음, 각 라인의 맨 처음과 매치 된다
# $는 문자열의 맨 끝, 각 라인의 맨 끝과 매치
# S, DOT ALL .을 줄바꾸기 문자도 포함하여 매치하게 한다
# U, UNICODE \w, \W, \b, \B가 유니코드 문자 특성에 의존하게 한다
# X, VERBOSE 정규식 안의 공백은 무시된다

import re

def fn2():
    s1 ='apple ki\ni banna straw'
    match = re.search('ki.i', s1, re.DOTALL ) # ki, i 사이에 한개의문자가 뭐가와도 찾아준다 (개행조차!)
    print( match.group() )

def fn3():
    s1 ='apple kiwi banna straw'
    match = re.search('AP*LE', s1, re.IGNORECASE) #re.I
    # 대소문자 구문 안하곘다!
    print( match.group())


def fn4():
    s1 ='''lg hi test
hello korea
lg first
python test
lg python
'''
    print(s1)
    # 문자의 시작이 매 개행마다 적용됨
    my = re.findall('^lg\s\w+', s1,  re.MULTILINE)
    print( my )



