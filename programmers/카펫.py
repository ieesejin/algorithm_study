# https://programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, yellow):
    for i in range(3, int((brown + yellow) / 2)): # x >= y, i -> y
        if (brown + yellow) % i != 0: # When divided
            continue

        y = i
        x = (brown + yellow) // y

        if (x - 2) * (y - 2) == yellow:
            return [x, y]


print(solution(8, 1)) # expected value: [3, 3]