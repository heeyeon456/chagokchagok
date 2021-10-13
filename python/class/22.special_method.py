# special method
# object 의 멤버함수
class Test: #object
    def __init__(self):
        print("init call")
        self.a = 0
        self.b = 0
        self.myDic = {} #공백 dictionary
    def setData(self,x,y):
        self.a = x
        self.b = y
    def show(self):
        print(self.a, self.b)

    # 상위 클래스 object 에 있는거 재정의
    def __repr__(self):
        return f'a={self.a} b={self.b}'

    def __add__(self, other):
        print('add call')
        return self.a + other

    def __setitem__(self, key, value):
        print('setitem call')
        self.myDic[key] = value

    def __getitem__(self, item):
        return self.myDic[item]


obj = Test()
print(obj) # obh.__repr__()
obj['aa'] = 10 # obj.__setitem('aa', 10)
obj['bb'] = 20 # obj.__setitem('bb', 10)
print(obj['aa']) #obj.__getitem__('aa')
print(obj.myDic)
# d = {'aa': 1}
# d['aa'] = 10 # 있으면 수정
# d['bb'] = 20 # 없으면 추가

"""
obj = Test()
print( obj ) # obj.__repr__() 로 바꿔줌
obj.setData(10, 20)
rst = obj+100 # obj.__add__(100)
print(rst)

# 문자열 클래스 객체
s = 'abc'
print(s+'def') # special method 로 두개의 문자열에 연결되도록 정의되어 있음



# 파이썬에서 변수는 객체 또는 레퍼런스
# my = [10,20,30,40]  # 힙메모리에 리스트 클래스 객체 할당
# print( my )
"""
