# https://www.acmicpc.net/problem/11660


import sys
input = sys.stdin.readline


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if not y and x:
            board[y][x] = board[y][x-1] + board[y][x]
        elif y and not x:
            board[y][x] = board[y-1][x] + board[y][x]
        elif y and x:
            board[y][x] = board[y][x] + board[y-1][x] + board[y][x-1] - board[y-1][x-1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    y1 -= 1
    x1 -= 1
    y2 -= 1
    x2 -= 1

    if y1 == 0 and x1 == 0:
        print(board[y2][x2])
    elif y1 != 0 and x1 == 0:
        print(board[y2][x2] - board[y1-1][x2])
    elif y1 == 0 and x1 != 0:
        print(board[y2][x2] - board[y2][x1-1])
    elif y1 != 0 and x1 != 0:
        print(board[y2][x2] - board[y2][x1-1] - board[y1-1][x2] + board[y1-1][x1-1])
