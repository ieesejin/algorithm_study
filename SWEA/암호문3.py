# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14zIwqAHwCFAYD&categoryId=AV14zIwqAHwCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8
from collections import deque


for test_case in range(10):
    N = int(input())
    encrypt = list(input().split())
    commands_num = int(input())
    commands = deque(list(input().split()))

    while commands:
        command = commands.popleft()
        if command == 'I':
            x = int(commands.popleft())
            y = int(commands.popleft())
            pop_list = []
            for i in range(y):
                temp = commands.popleft()
                pop_list.append(temp)
            encrypt = encrypt[:x] + pop_list + encrypt[x:]

        if command == 'D':
            x = int(commands.popleft())
            y = int(commands.popleft())
            encrypt = encrypt[:x] + encrypt[x+y:]

        if command == 'A':
            y = int(commands.popleft())
            pop_list = []
            for i in range(y):
                temp = commands.popleft()
                pop_list.append(temp)
            encrypt += pop_list

    print("#{}".format(test_case+1), end=" ")
    for i in range(10):
        print("{}".format(encrypt[i]), end=" ")