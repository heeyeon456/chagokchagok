#LGB 규칙
# local > global > built-in
g = 10
def fn():
    global g
    g = 100
    print("g=", g)
fn()
print("함수 호출 후 g=", g)
