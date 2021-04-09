# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9


for test_case in range(10):
    dump = int(input())
    heights = list(map(int, input().split()))

    for i in range(dump):
        heights[heights.index(max(heights))] -= 1
        heights[heights.index(min(heights))] += 1

    print("#{} {}".format(test_case+1, max(heights)-min(heights)))
