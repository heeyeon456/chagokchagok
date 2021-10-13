import re
s1 ='aaa-bbb#ccc.ddd eee'
s2 = 'i like apple like application'

s = re.split('[ #.-]', s1)
print(s)

# rs = re.sub('ap\w+', 'love', s2)
def fn( m ):
    print ("m=", m)
    if m.group() == 'apple':
        return 'test'
    else: return 'test1'

rs = re.sub('ap\w+', fn, s2)
rs = re.sub('ap\w+',
     lambda m:'test' if m.group()=='apple' else 'test1', s2)
print(rs)
