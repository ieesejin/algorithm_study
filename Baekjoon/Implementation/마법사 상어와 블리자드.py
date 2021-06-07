# https://www.acmicpc.net/problem/21611


import sys
input = sys.stdin.readline


def boardToList(board):
    sy, sx = 0, 0
    res = []
    eswn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(N-1, 0, -2):
        for j in range(4):
            for k in range(i):
                res.append(board[sy][sx])
                sy += eswn[j][0]
                sx += eswn[j][1]
        sy += 1
        sx += 1

    return res


def listToBoard(newList):
    sy, sx = 0, 0
    res = [[0 for _ in range(N)] for _ in range(N)]
    eswn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(N - 1, 0, -2):
        for j in range(4):
            for k in range(i):
                res[sy][sx] = newList.pop()
                sy += eswn[j][0]
                sx += eswn[j][1]
        sy += 1
        sx += 1

    return res


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
point = 0

for i in range(M):

    d, power = map(int, input().split())

    # 얼음파편 스킬
    for j in range(1, power+1):
        dy, dx = direction[d][0], direction[d][1]
        board[(N-1)//2 + dy*j][(N-1)//2 + dx*j] = 0

    boardList = boardToList(board)

    while 0 in boardList:
        boardList = [num for num in boardList if num] # 0을 다 지워줌

        if len(boardList) < 4:
            break

        continueCount = 1
        continueNums = boardList[0]
        for k in range(1, len(boardList)):
            if boardList[k] == continueNums:
                continueCount += 1
            else:
                if continueCount >= 4:
                    for m in range(1, continueCount+1):
                        point += boardList[k-m]
                        boardList[k-m] = 0
                continueCount = 1
                continueNums = boardList[k]
        if continueCount >= 4:
            for m in range(1, continueCount + 1):
                point += boardList[-m]
                boardList[-m] = 0

    boardList.reverse()
    if len(boardList) == 0:
        break
    if len(boardList) == 1:
        newList = [1, boardList[0]]
    else:
        continueCount = 1
        continueNum = boardList[0]
        newList = []
        for j in range(1, len(boardList)):
            if boardList[j] == continueNum:
                continueCount += 1
            else:
                newList.append(continueCount)
                newList.append(continueNum)
                continueCount = 1
                continueNum = boardList[j]
        if continueCount != 1:
            newList.append(continueCount)
            newList.append(continueNum)

        if len(newList) > N**2-1:
            newList = newList[:N**2-1]
        else:
            while len(newList) != N**2-1:
                newList.append(0)

    board = listToBoard(newList)

print(point)
