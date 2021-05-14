# https://www.acmicpc.net/problem/17829


import sys
import copy
input = sys.stdin.readline


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

while True:
    new_board = []

    for y in range(N//2):
        new_row = []
        for x in range(N//2):
            temp = sorted([board[2*y][2*x], board[2*y][2*x+1], board[2*y+1][2*x], board[2*y+1][2*x+1]])
            new_row.append(temp[2])
        new_board.append(new_row)

    if len(new_board) == 1:
        print(new_board[0][0])
        break

    board = copy.deepcopy(new_board)
    N = N//2
