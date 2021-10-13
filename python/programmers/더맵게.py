import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    mix = lambda x1, x2 : x1 + 2*x2

    while scoville[0] < K and len(scoville) >= 1:
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville, mix(x1, x2))
        answer += 1
        print(answer, scoville)
        
    if scoville[0] < K:
        answer = -1


    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))

