# https://www.acmicpc.net/problem/2748


import sys
input = sys.stdin.readline


n = int(input())
dp = []

for i in range(n+1):
    if i == 0:
        dp.append(0)
    elif i == 1:
        dp.append(1)
    else:
        dp.append(dp[i-1] + dp[i-2])

print(dp[-1])
