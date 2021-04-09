# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9\


def check(li):
    res = True

    for i in range(len(li)//2 + 1):
        if li[i] != li[-(i+1)]:
            res = False
            break

    return res


for test_case in range(10):
    case_num = int(input())
    board = []
    for i in range(100):
        board.append(list(input()))

    max_len = 0
    length = len(board)
    for row in board:
        for i in range(length):
            for j in range(length, i, -1):
                if check(row[i:j]):
                    max_len = max(max_len, len(row[i:j]))
                    break
            if length - i < max_len:
                break

    board = list(map(list, zip(*board)))
    for col in board:
        for i in range(length):
            for j in range(length, i, -1):
                if check(col[i:j]):
                    max_len = max(max_len, len(col[i:j]))
                    break
            if length - i < max_len:
                break

    print("#{} {}".format(case_num, max_len))
