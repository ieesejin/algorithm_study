# https://www.acmicpc.net/problem/13460


from collections import deque


def move(y_, x_, dy_, dx_):
    count = 0
    while board[y_+dy_][x_+dx_] != '#' and board[y_][x_] != 'O':
        x_ += dx_
        y_ += dy_
        count += 1
    return y_, x_, count


def bfs():
    q = deque([(pos_by, pos_bx, pos_ry, pos_rx, 0)])
    while q:
        by, bx, ry, rx, depth = q.popleft()
        if depth >= 10:
            break
        for i in range(4):
            nby, nbx, bcount = move(by, bx, dy[i], dx[i])
            nry, nrx, rcount = move(ry, rx, dy[i], dx[i])
            if board[nby][nbx] == 'O':
                continue
            if board[nry][nrx] == 'O':
                print(depth + 1)
                return
            if nby == nry and nbx == nrx:
                if bcount > rcount:
                    nby -= dy[i]
                    nbx -= dx[i]
                else:
                    nry -= dy[i]
                    nrx -= dx[i]

            if (nby, nbx, nry, nrx) not in visited:
                visited.add((nby, nbx, nry, nrx))
                q.append((nby, nbx, nry, nrx, depth + 1))
    print(-1)


N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
pos_by, pos_bx = 0, 0
pos_ry, pos_rx = 0, 0

for y in range(N):
    for x in range(M):
        if board[y][x] == 'B':
            pos_by, pos_bx = y, x
        if board[y][x] == 'R':
            pos_ry, pos_rx = y, x

visited = set()
bfs()
