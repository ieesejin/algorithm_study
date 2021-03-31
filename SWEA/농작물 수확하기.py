# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GLXqKAWYDFAXB&categoryId=AV7GLXqKAWYDFAXB&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7


T = int(input())
answer = []

for test_case in range(T):
    N = int(input())
    farm = []
    # for i in range(N):
    #     farm.append(input())
    #
    # total = 0
    # for j in range(int((N-1)/2)+1):
    #     total += int(farm[j][int((N - 1) / 2)])
    #     for x in range(j):
    #         total += int(farm[j][int((N - 1) / 2) + (x+1)])
    #         total += int(farm[j][int((N - 1) / 2) - (x+1)])
    #
    # for k in range(int((N-1)/2)):
    #     total += int(farm[-(k+1)][int((N-1)/2)])
    #     for x in range(k):
    #         total += int(farm[-(k+1)][int((N - 1) / 2) + (x+1)])
    #         total += int(farm[-(k+1)][int((N - 1) / 2) - (x+1)])
    #
    # answer.append(total)
    for i in range(N):
        farm.append(list(map(int, list(input()))))

    total = 0
    for j in range(N // 2 + 1):
        total += sum(farm[j][N//2 - j:N//2 + j + 1])

    for k in range(N // 2):
        total += sum(farm[-(k+1)][N//2 - k:N//2 + k + 1])

    answer.append(total)

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
