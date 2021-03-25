# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBOHEx66kIDFAWr&categoryId=AWBOHEx66kIDFAWr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6


T = int(input())
answer = []

for test_case in range(T):
    str1, str2 = input().split(" ")

    dp = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    # for i in range(1, len(dp)):
    #     for j in range(1, len(dp[i])):
    #         if str2[i-1] == str1[j-1]:
    #             dp[i][j] = dp[i-1][j-1] + 1
    #         else:
    #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 두 문자열의 길이가 다를 때를 잘 생각해서 dp의 가로 세로를 잘 구분해야됨.
    # LIS ( Longest Increasing Subsequence) 알고리즘 이해
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]: # 같은 문자열일 때
                dp[j+1][i+1] = dp[j][i] + 1
            else:
                dp[j+1][i+1] = max(dp[j+1][i], dp[j][i+1])

    answer.append(dp[-1][-1])

# 출력
for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
