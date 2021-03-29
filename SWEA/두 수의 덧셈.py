# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWBC1lOad9IDFAWr&categoryId=AWBC1lOad9IDFAWr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6


T = int(input())
answers = []

for test_case in range(T):
    a, b = map(int, input().split(" "))
    answers.append(a+b)


for i in range(len(answers)):
    print("#{} {}".format(i+1, answers[i]))
