# https://www.acmicpc.net/problem/2167

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for x in range(1, M):
    board[0][x] += board[0][x-1]
for y in range(1, N):
    board[y][0] += board[y-1][0]
for y in range(1, N):
    for x in range(1, M):
        board[y][x] += board[y][x-1] + board[y-1][x] - board[y-1][x-1]

for case in range(int(input())):
    i, j, x, y = map(int, input().split())

    if i == 1 and j == 1:
        print(board[x-1][y-1])
    elif i == 1 and j != 1:
        print(board[x-1][y-1] - board[x-1][j-2])
    elif j == 1 and i != 1:
        print(board[x-1][y-1] - board[i-2][y-1])
    elif i > 1 and j > 1 and x > 1 and y > 1:
        print(board[x-1][y-1] - board[x-1][j-2] - board[i-2][y-1] + board[i-2][j-2])


