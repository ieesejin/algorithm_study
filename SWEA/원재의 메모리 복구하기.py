# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV19AcoKI9sCFAZN&categoryId=AV19AcoKI9sCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8


T = int(input())
answer = []

for test_case in range(T):
    memory = input()
    count = 0
    flag = 0
    for m in memory:
        if m == '0' and flag == 1:
            count += 1
            flag = 0
        if m == '1' and flag == 0:
            flag = 1
            count += 1

    answer.append(count)

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
