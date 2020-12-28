# https://programmers.co.kr/learn/courses/30/lessons/68645


def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = -1
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # down side
                y += 1

            if i % 3 == 1:  # right side
                x += 1

            if i % 3 == 2:  # up side
                x -= 1
                y -= 1

            answer[y][x] = num
            num += 1

    answer = [j for i in answer for j in i if j != 0]

    return answer


print(solution(4))
