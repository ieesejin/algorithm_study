# https://www.acmicpc.net/problem/2178


from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0, 1))
    res = []

    while q:
        y, x, count = q.popleft()
        if y == N-1 and x == M-1:
            res.append(count)
            continue

        for dy, dx in (1, 0), (0, 1), (-1, 0), (0, -1):
            ny, nx = y + dy, x + dx
            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and visited[ny][nx] != 1 and board[ny][nx] == 1:
                q.append((ny, nx, count+1))
                visited[ny][nx] = 1
    return res


N, M = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
print(min(bfs()))
