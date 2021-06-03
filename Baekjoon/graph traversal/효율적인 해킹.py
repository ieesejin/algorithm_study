# https://www.acmicpc.net/problem/1325


import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def dfs(start_node):
    global graph

    visited = [0 for _ in range(N+1)]
    stack = deque()
    stack.append(start_node)
    visited[start_node] = 1
    hacking = 1
    while stack:
        cur_node = stack.pop()
        if cur_node not in graph:
            continue
        for node in graph[cur_node]:
            if not visited[node]:
                visited[node] = 1
                hacking += 1
                stack.append(node)

    return hacking


N, M = map(int, input().split())

graph = defaultdict(list)
for i in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

answer = []
max_hack = 0
for i in range(1, N+1):
    hacking = dfs(i)
    if max_hack < hacking:
        answer = [i]
        max_hack = hacking
    elif max_hack == hacking:
        answer.append(i)

answer.sort()

print(*answer)
