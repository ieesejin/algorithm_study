# # https://www.acmicpc.net/problem/11725
#
# solve with recursive
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def makeTree(start_node):
    global parent, visited
    visited[start_node] = 1
    for node in graph[start_node]:
        if visited[node] == 1:
            continue
        parent[node] = start_node
        makeTree(node)


N = int(input().rstrip())
graph = defaultdict(list)
for i in range(N-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for i in range(N+1)]
parent = [i for i in range(N+1)]
makeTree(1)

for i in range(2, len(parent)):
    print(parent[i])


# solve with bfs
# import sys
# from collections import defaultdict, deque
# input = sys.stdin.readline
#
#
# def bfs(start):
#     q = deque([start])
#     visited = [0 for _ in range(N + 1)]
#     parent = [_ for _ in range(N + 1)]
#     visited[start] = 1
#     while q:
#         p = q.popleft()
#         for node in graph[p]:
#             if visited[node] == 1:
#                 continue
#             parent[node] = p
#             q.append(node)
#             visited[node] = 1
#
#     return parent
#
#
# N = int(input().rstrip())
# graph = defaultdict(list)
# for i in range(N-1):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)
#
# answer = bfs(1)
# for i in range(2, len(answer)):
#     print(answer[i])

