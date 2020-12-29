# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville) # heapq

    while True:
        if len(scoville) == 1 or scoville[0] >= K: # loop end condition
            break

        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1

    if scoville[0] < K: # cannot make spicy
        return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7)) # expected result: 2 (1, 2) -> 5, (5, 3) -> 13
