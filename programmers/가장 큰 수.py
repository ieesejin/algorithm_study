# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
    numbers = list(map(str, numbers)) # int to string -> for use sort
    numbers = sorted(numbers, key=lambda x: x * 3, reverse=True) # sort with key -> Because of max digit is 4 use (x * 3)

    answer = ''.join(numbers) # list to string with ''

    if int(answer) == 0: # [0, 0, 0] case
        return '0'

    return answer


print(solution([3, 30, 34, 5, 9]))
