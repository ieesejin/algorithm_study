# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWAe5G8afT0DFAUw&categoryId=AWAe5G8afT0DFAUw&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6


T = int(input())
answers = []

for test_case in range(T):
    A, B = map(int, input().split(" "))
    answers.append(int((A/B) ** 2))

for i in range(len(answers)):
    print("#{} {}".format(i+1, answers[i]))
