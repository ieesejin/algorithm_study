# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9


for test_case in range(10):
    length = int(input())
    heights = list(map(int, input().split()))
    count = 0
    for i in range(2, length-2):
        temp = [heights[i-2], heights[i-1], heights[i+1], heights[i+2]]
        if heights[i] - max(temp) > 0:
            count += heights[i] - max(temp)

    print("#{} {}".format(test_case + 1, count))
