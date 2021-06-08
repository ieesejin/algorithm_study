# https://www.acmicpc.net/problem/1647


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


V, E = map(int, input().split())

parent = [x for x in range(V+1)]
rank = [0 for x in range(V+1)]

edges = []
for edge in range(E):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[2])

mst = []
for edge in edges:
    a, b, c = edge
    if find(a) != find(b):
        union(a, b)
        mst.append(c)

print(sum(mst) - max(mst))
