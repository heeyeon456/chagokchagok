def fn():
    print('hello')
    print('hello')

# 인자, argument
def hap(a, b):
    return a+b

rst = hap(10, 20)
print(rst)

def get_fat(height: int,
            weight: int):
    unit_weight = (height-100)*0.85
    fat_ratio = weight * 100 / unit_weight
    status = None
    if fat_ratio < 90:
        status = "저체증"
    elif 90 <= fat_ratio <= 110:
        status = "정상"
    elif 110 < fat_ratio <= 120:
        status = "과체중"
    else:
        status = "비만"
    print("현재 상태를 %s 입니다. " % status )
    return status

