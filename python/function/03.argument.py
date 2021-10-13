# 가변인자 : 넘겨주는 개수에 제한이 없음
def fn( *args):
    print(args)

def circles( *rs):
    return [3.14*r**2 for r in rs]

def onlyeven( *nums):
    return [n for n in nums if n % 2 == 0 ]

def fn1(*values, a=1, b=1):
    print(values)
    print("a=", a)
    print("b=", b)

fn('aa', 'bb', 'cc')
rst = circles(1,2,3,4,5)
print(rst)
rst = onlyeven(1,2,3,4,5,6)
print(rst)

print(1,2,3,sep='-')
print('hello', end=' ')
fn1(1,2,3,4,5)
fn1(1,2,3,a=4,b=5)
