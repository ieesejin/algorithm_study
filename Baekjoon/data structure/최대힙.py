# https://www.acmicpc.net/problem/11279


import heapq
import sys
input = sys.stdin.readline


N = int(input())

hq = []
for i in range(N):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, (-num, num))