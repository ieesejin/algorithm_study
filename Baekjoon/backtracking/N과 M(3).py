# https://www.acmicpc.net/problem/15651


from itertools import product
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
nums = [i+1 for i in range(N)]
argu = [nums for _ in range(M)]

p = product(*argu) # p = product(nums, repeat=M)

for i in p:
    print(*i)
