# https://programmers.co.kr/learn/courses/30/lessons/72413


import heapq  # 다익스트라 알고리즘에 사용
import math  # 무한대 정의에 사용


def solution(n, s, a, b, fares):
    answer = math.inf
    graph = [[] for _ in range(n + 1)]  # 위치간 거리를 그래프화
    for fare in fares:
        src, dst, distance = fare[0], fare[1], fare[2]
        graph[src].append([dst, distance])
        graph[dst].append([src, distance])

    for i in range(1, n + 1):  # 출발지점에서 모든 점까지 최단거리를 구하고 그 점에서 각 a, b 까지의 최단거리를 구해서 최솟값을 구함
        answer = min(answer, dijkstra(graph, s, i) + dijkstra(graph, i, a) + dijkstra(graph, i, b))

    return answer


def dijkstra(graph, s, d):  # s에서 출발해 d까지 가는 최단 거리
    table = [math.inf for _ in range(len(graph))]  # s에서 출발해서 각 점까지 일단 무한대로 정의
    table[s] = 0  # 자기 자신까지 거리는 0
    hq = [[0, s]]  # 자기 자신에서 갈 수 있는 곳을 찾기 위해 시작은 자기 자신 부터

    while hq:  # 갈 수 있는 곳이 끝날 때 까지
        dist, start = heapq.heappop(hq)

        if table[start] < dist:
            continue  # 이미 더 짧게 갈 수 있는 경우가 있으면 패스

        for point in graph[start]:
            next_start, next_dist = point[0], point[1]
            next_dist += dist  # start에서 갈 수 있는 다음 점까지 거리를 더함
            if next_dist < table[next_start]:  # 더한 값이 다른 방법들 보다 짧으면 짧은 값으로 다시 초기화
                table[next_start] = next_dist
                heapq.heappush(hq, [next_dist, next_start])  # 다음 점에서 갈 수 있는 곳을 추가

    return table[d]


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # expected result: 82
