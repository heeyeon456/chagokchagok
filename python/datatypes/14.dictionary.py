d = {'aa':10, 'bb':20, 'cc':30}
print(d)
print(type(d))
print(d['aa'])
print(d.keys())
print(d.values())
print(d.items())
d.pop('aa')
print(d)
print(d.get('ff', 1000))
