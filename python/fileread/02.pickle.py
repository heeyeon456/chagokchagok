import pickle

def obWrite():
    # 객체 저장
    my = [10, 20, 30, 40, 50]
    fp = open('ob.txt', 'wb')
    pickle.dump(my, fp) # heap memory 에 있는 걸 그대로 하드디스크에 저장
    fp.close()

def obRead():
    fp = open('ob.txt', 'rb')
    rd = pickle.load(fp) # 하드디스트의 리스트 객체를 힙메모리에 저장하고, 메모리의 참조계수 반환
    fp.close()
    print(rd)

obWrite()
obRead()
