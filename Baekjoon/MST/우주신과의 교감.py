# https://www.acmicpc.net/problem/1774


import sys
input = sys.stdin.readline


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_a, node_b):
    a = find(node_a)
    b = find(node_b)
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1


N, M = map(int, input().split())
vertex = []
parent = [_ for _ in range(N+1)]
rank = [0 for _ in range(N+1)]

for _ in range(N):
    vertex.append(list(map(int, input().split())))

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

edges = []
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = vertex[i]
        x2, y2 = vertex[j]
        edges.append([i+1, j+1, ((x2-x1)**2 + (y2-y1)**2)**0.5])

mst = 0
edges.sort(key=lambda x: x[2])
for edge in edges:
    a, b, w = edge
    if find(a) != find(b):
        union(a, b)
        mst += w
print(edges)
print('%.2f' % mst)
