my = [10, 20, 30, 40, 50]
my.append(60)
my.append(70)
my.insert(1, 100) # 중간추가 (1번 자리에 100 추가)
my.remove(30) # 요소로 삭제
my.pop(0)  # 인덱스로 삭제
print(my)
print(my.count(20))
print(my.index(100))
print(len(my)) # 전체 데이터 요소의 개수

