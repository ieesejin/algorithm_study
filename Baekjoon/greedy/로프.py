# https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline


N = int(input())

lopes = [int(input()) for _ in range(N)]
lopes.sort(reverse=True)

max_weight = 0
length = len(lopes)
for i in range(length):
    max_weight = max(lopes[i]*(i+1), max_weight)

print(max_weight)
