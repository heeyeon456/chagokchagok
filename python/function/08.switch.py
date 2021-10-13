# 다른 언어
def fn1():
    print('fn1 call')

def fn2():
    print('fn2 call')
def defaultFn():
    print("defaultFn call")

menu = {1:fn1, 2:fn2}
#menu[2]()
menu.get(1, defaultFn)()
