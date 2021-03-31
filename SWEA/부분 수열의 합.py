# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7


from itertools import combinations

T = int(input())
answer = []

for test_case in range(T):
    count = 0
    N, K = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))
    for i in range(1, N+1):
        if i > K:
            break
        combs = list(combinations(nums, i))
        for comb in combs:
            if sum(comb) == K:
                count += 1

    answer.append(count)

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
