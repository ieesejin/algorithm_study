# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14jJh6ACYCFAYD&categoryId=AV14jJh6ACYCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8

from collections import Counter

T = int(input())
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(T):
    case_num, length = input().split()
    case = list(input().split())
    case_dict = Counter(case)
    answer = []
    for i in num:
        answer += [i] * case_dict[i]

    print(case_num, end=" ")
    for i in range(len(answer)):
        print("{}".format(answer[i]), end=" ")
