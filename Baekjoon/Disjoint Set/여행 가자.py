# https://www.acmicpc.net/problem/1976


import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(start_node):
    go = [0 for _ in range(N)]
    stack = [start_node]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if go[i] != 1:
                go[i] = 1
                stack.append(i)

    return go


N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

graph = defaultdict(list)
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            graph[i].append(j)
            graph[j].append(i)

can_go = []

for i in range(N):
    can_go.append(dfs(i))

print(can_go)

route = list(map(int, input().split()))

answer = 'YES'
for i in range(M-1):
    if route[i] == route[i+1]:
        continue
    if not can_go[route[i]-1][route[i+1]-1]:
        answer = 'NO'
        break

print(answer)
