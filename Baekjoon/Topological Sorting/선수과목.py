# https://www.acmicpc.net/problem/14567

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

subject = [1 for _ in range(N+1)]

prerequisite = []
for i in range(M):
    A, B = map(int, input().split())
    prerequisite.append((A, B))


prerequisite.sort(key=lambda x: x[0])
for A, B in prerequisite:
    subject[B] = max(subject[B], subject[A] + 1)

print(' '.join(map(str, subject[1:])))
