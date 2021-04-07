# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

from collections import deque

for test_case in range(10):
    T = int(input())
    password = deque(list(map(int, input().split())))

    cycle = 1
    while password[-1]:
        x = password.popleft() - cycle
        if x < 0:
            x = 0

        password.append(x)

        cycle += 1
        if cycle == 6:
            cycle = 1

    print("#{}".format(test_case+1), end=" ")
    for i in range(len(password)):
        print("{}".format(password[i]), end=" ")
