# https://programmers.co.kr/learn/courses/30/lessons/12899


def toTenary(x):
    str_te = ''

    while x != 0:
        if x % 3 == 2:
            str_te = '2' + str_te
            x = x // 3

        elif x % 3 == 1:
            str_te = '1' + str_te
            x = x // 3

        elif x % 3 == 0:
            str_te = '0' + str_te
            x = x // 3

    return str_te


def solution(n):
    answer = ''
    x = list(toTenary(n))

    for i in range(len(x) - 1, 0, -1):
        if x[i] == '4':
            x[i] = '2'
            if x[i - 1] == '0':
                x[i - 1] = '4'
            elif x[i - 1] == '1':
                x[i - 1] = '0'
            elif x[i - 1] == '2':
                x[i - 1] = '1'

        if x[i] == '0':
            x[i] = '4'
            if x[i - 1] == '0':
                x[i - 1] = '4'
            elif x[i - 1] == '1':
                x[i - 1] = '0'
            elif x[i - 1] == '2':
                x[i - 1] = '1'

    answer = str(int(''.join(x)))

    return answer


print(solution(4)) # expected result: 11