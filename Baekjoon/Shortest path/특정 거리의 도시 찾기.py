# https://www.acmicpc.net/problem/18352


import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    inf = 1e9
    d = [inf for _ in range(N+1)]
    d[start] = 0
    hq = []
    heapq.heappush(hq, [d[start], start])
    while hq:
        cur_distance, cur_destination = heapq.heappop(hq)
        # if d[cur_destination] < cur_distance:
        #     continue
        if cur_destination in graph:
            for new_destination in graph[cur_destination]:
                distance = cur_distance + 1
                if distance < d[new_destination]:
                    d[new_destination] = distance
                    heapq.heappush(hq, [distance, new_destination])

    return d


N, M, K, X = map(int, input().split())

graph = dict()
for i in range(M):
    s, e = map(int, input().split())
    if s not in graph:
        graph[s] = [e]
    else:
        graph[s].append(e)

shortest_path = dijkstra(X)

answer = []
for i in range(len(shortest_path)):
    if shortest_path[i] == K:
        answer.append(i)

if not len(answer):
    print(-1)
else:
    for i in sorted(answer):
        print(i)
