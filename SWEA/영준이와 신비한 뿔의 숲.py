# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV_6xWk6sbADFAWS&categoryId=AV_6xWk6sbADFAWS&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6


T = int(input())
answers = []

for test_case in range(T):
    n, m = map(int, input().split(" "))
    a = n-m
    b = 2*m-n
    answers.append((b, a))

for i in range(len(answers)):
    print("#{} {} {}".format(i+1, answers[i][0], answers[i][1]))
