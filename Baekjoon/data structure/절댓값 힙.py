# https://www.acmicpc.net/problem/11286

import sys
import heapq
input = sys.stdin.readline


hq = []
N = int(input())
for i in range(N):
    num = int(input())
    if num:
        heapq.heappush(hq, (abs(num), num))
    elif not num:
        if not hq:
            print(0)
        else:
            p = heapq.heappop(hq)
            print(p[1])
