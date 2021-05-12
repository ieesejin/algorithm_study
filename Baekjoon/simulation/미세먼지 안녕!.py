# https://www.acmicpc.net/problem/17144
# python(시간초과) pypy(통과)


import sys
import copy


input = sys.stdin.readline
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

conditioner = []

for r in range(R):
    if board[r][0] == -1:
        conditioner.append(r)

for t in range(T):
    new_board = [[0 for _ in range(C)] for _ in range(R)]

    # 퍼지는 부분
    for r in range(R):
        for c in range(C):
            if board[r][c] and board[r][c] != -1:
                spread_sum = 0
                for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nr = r + dy
                    nc = c + dx
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        spread_sum += int(board[r][c]/5)
                        new_board[nr][nc] += int(board[r][c]/5)
                new_board[r][c] += board[r][c] - spread_sum
    new_board[conditioner[0]][0] = -1
    new_board[conditioner[1]][0] = -1

    # new_board 위쪽 처리
    cur_r, cur_c = conditioner[0] - 1, 0
    while True:
        if not cur_r:
            break
        new_board[cur_r][cur_c] = new_board[cur_r-1][cur_c]
        cur_r -= 1
    while True:
        if cur_c == C-1:
            break
        new_board[cur_r][cur_c] = new_board[cur_r][cur_c+1]
        cur_c += 1
    while True:
        if cur_r == conditioner[0]:
            break
        new_board[cur_r][cur_c] = new_board[cur_r+1][cur_c]
        cur_r += 1
    while True:
        if cur_c == 1:
            break
        new_board[cur_r][cur_c] = new_board[cur_r][cur_c-1]
        cur_c -= 1
    new_board[cur_r][cur_c] = 0

    # 아래쪽
    cur_r, cur_c = conditioner[1] + 1, 0
    while True:
        if cur_r == R-1:
            break
        new_board[cur_r][cur_c] = new_board[cur_r+1][cur_c]
        cur_r += 1
    while True:
        if cur_c == C-1:
            break
        new_board[cur_r][cur_c] = new_board[cur_r][cur_c+1]
        cur_c += 1
    while True:
        if cur_r == conditioner[1]:
            break
        new_board[cur_r][cur_c] = new_board[cur_r-1][cur_c]
        cur_r -= 1
    while True:
        if cur_c == 1:
            break
        new_board[cur_r][cur_c] = new_board[cur_r][cur_c-1]
        cur_c -= 1
    new_board[cur_r][cur_c] = 0

    board = copy.deepcopy(new_board)

answer = 0
for r in range(R):
    for c in range(C):
        if board[r][c] == -1:
            continue
        answer += board[r][c]

print(answer)
