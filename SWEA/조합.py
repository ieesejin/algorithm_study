# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGKdbqczEDFAUo&categoryId=AWXGKdbqczEDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9


import math


T = int(input())
for test_case in range(T):
    N, R = map(int, input().split())
    upper = math.factorial(N)
    lower = (math.factorial(R) * math.factorial(N-R)) ** (123456789-2)

    answer = upper * lower

    print("#{} {}".format(test_case+1, answer))
