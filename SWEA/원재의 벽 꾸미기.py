# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV2b9AkKACkBBASw&categoryId=AV2b9AkKACkBBASw&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7


T = int(input())
answer = []

for test_case in range(T):
    N, A, B = map(int, input().split())
    minimum = 100000000
    for i in range(1, N+1):
        j = 1
        while i * j <= N:
            minimum = min(minimum, A * abs(i - j) + B * (N - i * j))
            j += 1

    answer.append(minimum)

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
