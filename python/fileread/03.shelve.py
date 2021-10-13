# d = {}
# d['aa'] = 10
# d['bb'] = 20
# print(d)

# 윈도우에서 레지스트리에 저장
# 파이선에서는 key 값으로 프로그램 실행환경을 저장 가
import shelve

def shWrite():
    sh = shelve.open('my')
    sh['aa'] = 10
    sh['bb'] = 20
    sh['name'] = '홍길동'
    sh['age'] = 20
    sh['data'] = [(10, 20), (30, 40)]
    sh.close()

sh = shelve.open('my')
for k, v in sh.items():
    print(k, ":",  v)

#dictionary 의 멤버함수와 동일하게 활용 가능
sh.pop('aa')
for n in sh.keys():
    print(n)
