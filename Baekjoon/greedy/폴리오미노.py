# https://www.acmicpc.net/problem/1343


import sys
input = sys.stdin.readline


board = list(input())
count = 0
answer = ''
for i in board:
    if i == 'X':
        count += 1
    elif i == '.' or '\n':
        if count % 2:
            print(-1)
            break
        else:
            answer += 'AAAA' * (count // 4)
            if count % 4:
                answer += 'BB'
        answer += '.'
        count = 0
else:
    print(answer[:-1])
