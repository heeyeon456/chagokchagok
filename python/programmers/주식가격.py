def solution(prices):
    size = len(prices)
    answer = [0] * size
    for i in range(size):
        for j in range(i+1, size):
            answer[i] += 1
            if prices[i] > prices[j] :
                break

    return answer

prices = [1,4,2,3,2,5,1]
answer = solution(prices)
print(answer)

prices = [1,2,3,2,3]
answer = solution(prices)
print(answer)
