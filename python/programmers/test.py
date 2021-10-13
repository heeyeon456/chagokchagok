import heapq
import math
def solution(jobs):
    answer = 0
    jobs.sort()
    qu = []

    time = 0
    total_time = 0

    for start, delay in jobs:
       while (time < start or time == 0) and qu:
           d, s = heapq.heappop(qu)
           time += d
           total_time += (time - s)
           print("first: ", s, d, time - s)

       else:
           heapq.heappush(qu, (delay, start))



    while qu:
        delay, start = heapq.heappop(qu)
        if time < start:
            time = 0 if start > time + delay else start
            total_time += (time + delay)
            print("second: ", start, delay, time + delay)
        else:
            total_time += (time + delay - start)
            print("second: ", start, delay, time + delay - start)
        time += delay

    answer = math.floor(total_time / len(jobs))
    return answer


#[0, 10], [2,10], [9,10], [15,2] 의 작업 순서는 [0, 10], [2,10], [15,2], [9,10] 가 되어야 합니다.
#( [0, 10], [2,10], [9,10] 처리하고 나서 [15, 2] 기다리면 안됩니다)

#[0, 10], [2,10], [25,10], [25,2] 의 작업 순서는 [0, 10], [2,10], [25,2], [25,10] 가 되어야 합니다.
#(나중에 들어오는 [25,10], [25,2] 도 순서를 정해서 계산해야 합니다)
#jobs = [[0, 3], [1, 9], [2, 6]]
#jobs = [[0, 1], [1,7], [500, 6]]
#jobs = [[0, 10], [2, 10], [9, 10], [15, 2]]
jobs = [[0, 10], [2, 10], [25, 10], [25, 2]]
#jobs = [[0, 3], [4, 7], [1, 8]]
answer = solution(jobs)
print(answer)
