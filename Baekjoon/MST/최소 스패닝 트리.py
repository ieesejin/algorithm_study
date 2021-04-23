# https://www.acmicpc.net/problem/1197


from collections import defaultdict, deque
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
rank = [x for x in range(V+1)]

edges = []
for i in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

mst = 0
for edge in edges:
    node_a, node_b, weight = edge
    if find(node_a) != find(node_b):
        union(node_a, node_b)
        mst += weight

print(mst)
