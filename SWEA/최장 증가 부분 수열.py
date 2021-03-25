# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWBOKg-a6l0DFAWr

T = int(input())
answer = []

for test_case in range(T):
    N = int(input())
    sequence = list(map(int, input().split(" ")))

    dp = [1 for _ in range(N)]  # dp table

    for i in range(1, N):
        for j in range(i):
            if sequence[j] < sequence[i]:  # i 끝나는 위치 값이 j 끝나는 위치 값보다 크면 초기화
                dp[i] = max(dp[i], dp[j] + 1)

    answer.append(max(dp))

# 출력
for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
