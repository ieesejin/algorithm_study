# https://www.acmicpc.net/problem/2606


from collections import deque


computers = int(input())
links = int(input())

graph = {}
for i in range(links):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

visited = []

q = deque([1])
while q:
    p = q.popleft()
    if p in visited:
        continue
    visited.append(p)
    for computer in graph[p]:
        q.append(computer)

print(visited)

print(len(visited)-1)