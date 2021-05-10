# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1, len(nums)):
    nums[i] += nums[i-1]

for i in range(M):
    s, e = map(int, input().split())
    if s == 1:
        print(nums[e-1])
    else:
        print(nums[e-1] - nums[s-2])
