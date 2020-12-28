# https://programmers.co.kr/learn/courses/30/lessons/68644?language=python3


def solution(numbers):
    answer = set()

    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    return sorted(list(answer))


print(solution([2, 1, 3, 4, 1]))
# expected result = [2, 3, 4, 5, 6, 7]
