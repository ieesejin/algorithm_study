# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGEbd6cjMDFAUo&categoryId=AWXGEbd6cjMDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9


T = int(input())

for test_case in range(T):
    N = int(input())
    dummies = []
    for i in range(N):
        dummies.append(int(input()))

    move = 0
    same = sum(dummies)/len(dummies)
    for i in dummies:
        if i < same:
            move += same - i

    print("#{} {}".format(test_case+1, int(move)))
