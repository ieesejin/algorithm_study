# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV-Un3G64SUDFAXr&categoryId=AV-Un3G64SUDFAXr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7


T = int(input())
answer = []

for test_case in range(T):
    N, M = map(int, input().split(" "))
    N_set = set(input().split(" "))
    M_set = set(input().split(" "))

    answer.append(len(N_set.intersection(M_set)))

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
