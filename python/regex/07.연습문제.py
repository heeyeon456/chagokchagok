import re
s1 ='apple kiwi banna'
s2 ="123-abc def-ghi 346-Abc"
s3 ='<a href="my.html">abcde</a>' \
    '<font class="a.aa" size="10">'
s4 ="aaa ab.bcd.def.kim@gmail.com xxx aa@bb.aa"

#s3
# href뒤에 있는 파일명을 출력
# ex) aaa, aaa.txt, a132, aa_bc.my 파일.txt ..
# s4 이메일 주소 모두 찾

try:
    match = re.search('href="([\w.]+)"', s3)
    my = re.findall('[\w.]+@[\w.]+', s4)
    my = re.findall('([\w.]+)@[\w.]+', s4)
    print( match.group(1) )
    print(my)
except Exception as err:
    print("Not Found")

