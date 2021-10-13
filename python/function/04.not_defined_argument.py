def fn(**kwargs):
    print(kwargs)

def cylinder( **kwargs):
    return 3.14*kwargs['r']**2*kwargs['h']

fn(aa=10, bb=20)
fn(name='홍길동', age=20, addr='서울시')
print( cylinder(r=3, h=10) )
