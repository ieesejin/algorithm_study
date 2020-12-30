# https://programmers.co.kr/learn/courses/30/lessons/42747


def solution(citations):
    citations.sort(reverse=True) # To approach the maximum value

    for i in range(len(citations)):
        if citations[i] <= i:
            return i

    return len(citations)


print(solution([3, 0, 6, 1, 5])) # expected value: 3
