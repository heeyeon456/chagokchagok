def fn():
    return 10, 20
#디폴트 인자
def fn2(a=1, b=2):
    print(a, b)

fn2(10)
fn2(b=100)
