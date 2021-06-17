# https://www.acmicpc.net/problem/1010


from math import factorial
import sys
input = sys.stdin.readline


T = int(input())

# 팩토리얼 사용
# for test_case in range(T):
#     N, M = map(int, input().split())
#     print(factorial(M) // (factorial(N) * factorial(M-N)))

# 다이나믹 프로그래밍
for test_case in range(T):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1:
                dp[i][j] = j
            elif j >= i:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[N][M])
