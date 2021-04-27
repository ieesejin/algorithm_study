# https://www.acmicpc.net/problem/2839


N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(len(dp)):
    if i == 3 or i == 5:
        dp[i] = 1
    if i < 6:
        continue
    if dp[i-3] == 0 and dp[i-5] == 0:
        continue
    else:
        if dp[i-3] == 0:
            dp[i] = dp[i-5] + 1
        elif dp[i-5] == 0:
            dp[i] = dp[i-3] + 1
        else:
            dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if dp[-1] == 0:
    print(-1)
else:
    print(dp[-1])
