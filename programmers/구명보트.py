# https://programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 0

    light = sorted(people)
    start = 0 # forward index
    end = len(light) - 1 # backward index
    while start <= end:
        if light[start] + light[end] <= limit: # Two people on a boat case
            answer += 1
            start += 1
            end -= 1
        else: # One person on a boat case
            answer += 1
            end -= 1

    return answer


print(solution([70, 50, 80, 50], 100)) # expected value: 3
