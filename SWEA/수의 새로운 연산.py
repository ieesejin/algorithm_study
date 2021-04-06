# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7


def findByValue(value):
    if value == 1:
        return (1, 1)

    temp = 1
    temp_x = 0
    for i in range(2, 300):
        temp += i
        if temp >= value:
            temp_x = i
            break

    return (temp_x - (temp-value), 1 + (temp-value))


def findByLoc(x, y):
    result = 0
    for i in range(1, x+1):
        result += i
    for j in range(0, y-1):
        result += x + j

    return result


T = int(input())
answer = []

for test_case in range(T):
    p, q = map(int, input().split())
    px, py = findByValue(p)
    qx, qy = findByValue(q)

    answer.append(findByLoc(px+qx, py+qy))
    print(findByValue(10000))

for i in range(len(answer)):
    print("#{} {}".format(i+1, answer[i]))
