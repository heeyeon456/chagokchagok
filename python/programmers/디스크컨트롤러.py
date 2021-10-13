import heapq
from queue import PriorityQueue
import math

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, priority, item):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    def __repr__(self):
        return repr(self.queue)

def solution(jobs):
    answer = 0
    qu1 = PriorityQueue()
    qu2 = PriorityQueue()

    for start, time in jobs:
        qu1.push(start, time)
        qu2.push(time, start)
    total_time = 0
    for s, i, t in qu1.queue:
        total_time += (total_time + s + t)
    avg1 = total_time / len(jobs)

    total_time = 0
    print(qu2)
    for t, i, s in qu2.queue:
        total_time += (total_time + s - t)
    avg2 = total_time / len(jobs)

    print(avg1, avg2)




    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)




