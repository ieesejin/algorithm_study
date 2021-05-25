# https://www.acmicpc.net/problem/11403


import sys
from collections import defaultdict
input = sys.stdin.readline


def dfs(start_node):
    path = [0 for _ in range(N)]
    stack = [start_node]
    while stack:
        node = stack.pop()

        for link in graph[node]:
            if path[link] != 1:
                path[link] = 1
                stack.append(link)

    return path


graph = defaultdict(list)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if board[y][x] == 1:
            graph[y].append(x)

answer = []
for node in range(N):
    answer.append(dfs(node))

for row in answer:
    print(*row)
