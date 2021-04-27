# https://www.acmicpc.net/problem/15724

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, M):
    board[0][i] += board[0][i-1]
for j in range(1, N):
    board[j][0] += board[j-1][0]

for i in range(1, N):
    for j in range(1, M):
        board[i][j] += board[i-1][j] + board[i][j-1] - board[i-1][j-1]

K = int(input())
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(board[x2-1][y2-1])
    elif x1 == 1:
        print(board[x2-1][y2-1] - board[x2-1][y1-2])
    elif y1 == 1:
        print(board[x2-1][y2-1] - board[x1-2][y2-1])
    else:
        print(board[x2-1][y2-1] - board[x2-1][y1-2] - board[x1-2][y2-1] + board[x1-2][y1-2])

# for i in range(K):
#     sr, sc, er, ec = map(int, sys.stdin.readline().split())
#
#     if sr == 1 and sc == 1:
#         print(board[er - 1][ec - 1])
#     elif sr == 1:
#         print(board[er - 1][ec - 1] - board[er - 1][sc - 2])
#     elif sc == 1:
#         print(board[er - 1][ec - 1] - board[sr - 2][ec - 1])
#     else:
#         print(board[er - 1][ec - 1] - board[er - 1][sc - 2] - board[sr - 2][ec - 1] + board[sr - 2][sc - 2])