import re
s1 ='192.168.123.228 - - [01/Apr/2016:12:39:17 +0900] "GET /favicon.ico HTTP/1.1" 200 21630'
# 요청ip 사용자 이름 [요청시간 gmt] "요청방식(GET,POST) 요청문서 프로토콜" 응답코드 전송바이트사이즈
# ip 주소
try:
    # 1번
    # match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s1)
    # 2번
    # match = re.search('\d{2}/[a-zA-Z]+/\d{4}:\d{2}:\d{2}:\d{2} ', s1)
    # 3번
    # match = re.search(r'(GET|POST) /[\w.]+', s1)
    # match = re.search(r'(GET|POST) (/\S+)', s1)
    # print(match.group(2))
    # 4번
    #my = re.findall(r'[\d]+', s1)
    #print(my[-1])
    match = re.search(r'\d+$', s1)
    print(match.group())

except Exception as err:
    print("Not Found")


