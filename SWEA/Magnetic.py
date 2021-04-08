# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=8


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret


for test_case in range(10):
    width = int(input())
    board = []
    for i in range(width):
        temp = list(map(int, input().split()))
        board.append(temp)

    board = rotate_90(board)
    count = 0
    for row in board:
        temp = [x for x in row if x != 0]
        while True:
            if (temp[-1] == 1 and temp[0] == 2) or len(temp) == 0:
                break
            if temp[-1] == 2:
                temp.pop()
            if temp[0] == 1:
                temp.pop(0)

        count += ''.join(map(str, temp)).count('21')

    print("#{} {}".format(test_case+1, count))
