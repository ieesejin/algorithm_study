# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=9


for test_case in range(10):
    case_num = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    rotate_board = list(map(list, zip(*board)))

    sum_list = []
    cross_sum1 = 0
    cross_sum2 = 0

    for i in range(100):
        sum_list.append(sum(board[i]))
        sum_list.append(sum(rotate_board[i]))
        cross_sum1 += board[i][i]
        cross_sum2 += rotate_board[i][i]

    sum_list.extend([cross_sum1, cross_sum2])

    print("#{} {}".format(case_num, max(sum_list)))
