from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = list(map(lambda x, y: math.ceil((100 - x) / y), progresses, speeds))
    size = len(progresses)
    qu = deque()
    print("days", days)

    for i in range(size):
        qu.append(i)

    while len(qu) != 0:
        value = days[qu.popleft()]
        num = 1
        while len(qu) != 0 and value >= days[qu[0]]:
            qu.popleft()
            num += 1
        answer.append(num)


    return answer



progresses = [93, 30, 55]
speeds = [1, 30, 5]
answer = solution(progresses, speeds)
print(answer)

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
answer = solution(progresses, speeds)
print(answer)
