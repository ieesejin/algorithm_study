# https://www.acmicpc.net/problem/1717

import sys
input = sys.stdin.readline


def find(node):
    if set_list[node] != node:
        set_list[node] = find(set_list[node])
    return set_list[node]


def union(node_a, node_b):
    a = find(node_a)
    b = find(node_b)

    if rank[a] > rank[b]:
        set_list[b] = a
    else:
        set_list[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1


n, m = map(int, input().split())
set_list = [x for x in range(n+1)]
rank = [x for x in range(n+1)]

for i in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    if command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
