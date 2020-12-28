# https://programmers.co.kr/learn/courses/30/lessons/68935


def solution(n):
    answer = 0
    trinary = ''

    while n > 0:
        trinary += str(n % 3)
        n = n // 3

    trinary = list(trinary)
    trinary.reverse()

    for i in range(len(trinary)):
        answer += int(trinary[i]) * (3 ** i)

    return answer


print(solution(125))
