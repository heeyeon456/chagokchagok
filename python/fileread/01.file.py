def fileWrite2():
    fp =open('test.txt','w')
    print(fp.tell()) #위차값 확인
    fp.write('hello')
    fp.seek(2) # 2위치로 강제로 이동
    print(fp.tell()) #위차값 확인
    fp.write('korea')
    print(fp.tell()) #위차값 확인
    fp.close()

def fileRead2():
    fp =open('test.txt','r')
    rd = fp.read()
    fp.close()
    print( rd )

def fileWrite3():
    fp =open('test.txt','w')
    fp.write('abcdefghi')
    fp.close()

def fileRead3():
    fp =open('test.txt','r')
    rd = fp.read(3)
    fp.close()
    print( rd )

def fileWrite4():
    fp =open('test.txt','w')
    fp.write('abc\ndef\nghi')
    fp.close()
def fileRead4():
    fp =open('test.txt','r')
    for n in fp:
        print( n )
    # rd = fp.readline()
    # print( rd )
    # rd = fp.readline()
    # print( rd )
    fp.close()

def fileWrite5():
    fp =open('test.txt','w')
    fp.write('abc\ndef\nghi')
    fp.close()
def fileRead5():
    fp =open('test.txt','r')
    rd = fp.readlines()
    print( rd )
    fp.close()

# text 모드 코드 변형
# 10 (\n) --> 13(\r)
# 10 (\n) <-- 13, 10
# b mode ( 코드변형 x)
# 객체, 이미지, 동영상
def fileWrite6():
    fp = open('test.txt', 'wt')
    fp.write('kor\nea')
    fp.close()
def fileRead6():
    fp = open('test.txt','rt')
    rd = fp.read()
    fp.close()
    print(rd)
    print(len(rd))
fileWrite6()
fileRead6()
