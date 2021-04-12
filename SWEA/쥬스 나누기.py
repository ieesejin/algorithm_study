# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWXGAylqcdYDFAUo&categoryId=AWXGAylqcdYDFAUo&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9


T = int(input())

for test_case in range(T):
    N = int(input())
    print("#{}".format(test_case+1), end=" ")
    answer = "1/{} ".format(N) * N
    print(answer)


