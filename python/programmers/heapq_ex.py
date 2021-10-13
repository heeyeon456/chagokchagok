# 힙 : 각 노드가 하위 노드보다 작은 (또는 큰) 이진 트리
# 리스트에서 가장 작은 요소에 반복적으로 접근하는 프로그램

import heapq

# 리스트를 힙으로 바꾸기
list1 = [4, 6, 8, 1]
heapq.heapify(list1)
print(list1)

# 항목을 힙에 삽입, 제거
h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'have fun'))
heapq.heappush(h, (3, 'work'))
heapq.heappush(h, (4, 'study'))

print(heapq.heappop(list1))
for x in heapq.merge([1,3,5], [2,4,6]):
    print(x)

