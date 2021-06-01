# https://www.acmicpc.net/problem/1005

import sys
from collections import defaultdict
input = sys.stdin.readline


T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())
    D = [0]
    D.extend(list(map(int, input().split())))

    time = D[:]
    builds = []
    for i in range(K):
        x, y = map(int, input().split())
        builds.append((x, y))

    builds.sort()
    for build in builds:
        x, y = build
        time[y] = max(time[y], time[x] + D[y])

    W = int(input())

    print(time[W])
