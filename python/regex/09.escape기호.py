import re

s1 = 'apple kiwi banana appliacation'
try:
    myList = re.findall(r'\ba[a-z]+', s1) #\b 가 제어코드랑 겹침 r붙여줘야함
    # \b 는 단어의 경계에서 시작 -> banana의 anana는 출력이 안되게 됨
    myList = re.findall(r'\Ba[a-z]+', s1) # 단어의 경계가 아닌것
    print( myList )
except Exception as err:
    print("Not Found")
