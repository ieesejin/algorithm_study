# https://www.acmicpc.net/problem/15652


import sys
input = sys.stdin.readline


def backTracking(n, count):
    if count == M:
        print(*res)
        return
    for i in range(n, N):
        res.append(i+1)
        backTracking(i, count+1)
        res.pop()


N, M = map(int, input().split())
res = []
backTracking(0, 0)
