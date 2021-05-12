# https://www.acmicpc.net/problem/15650

from itertools import combinations


N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

combs = list(map(list, combinations(nums, M)))

for comb in combs:
    print(*comb)
