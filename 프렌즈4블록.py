# https://programmers.co.kr/learn/courses/30/lessons/17679


# 지워진 부분을 처리할때 편리하기 위해 돌리고 시작
def rotateBoard(m, n, board):
    table = []
    for i in range(n):
        temp = ''
        for j in range(m):
            temp += board[j][i]
        table.append(temp)

    return table


def find4Block(m, n, board, cnt):
    erasePoint = set() # 중복으로 지워지는 부분을 세지 않기 위해 집합으로 선언
    # 지울 부분을 erasePoint에 추가
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j].isalpha() and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                erasePoint.add((i, j))
                erasePoint.add((i, j+1))
                erasePoint.add((i+1, j))
                erasePoint.add((i+1, j+1))

    # 더이상 지울 부분이 없으면 리턴
    if len(erasePoint) == 0:
        return cnt

    # 지울 부분을 0으로 바꿔줌
    for y, x in erasePoint:
        board[y][x] = '0'

    # 지운 부분을 메꿈
    board = dropBlock(board)

    # 지울 부분이 없을 때까지 재귀
    return find4Block(m, n, board, len(erasePoint) + cnt)


# 0으로 지워진 부분을 메꿈
def dropBlock(board):
    board = [(line.count('0')) * '0' + "".join(line).replace("0", "") for line in board]
    board = [list(line) for line in board]
    return board


def solution(m, n, board):
    answer = 0
    board = rotateBoard(m, n, board)
    board = [list(line) for line in board]
    answer = find4Block(m, n, board, answer)

    return answer
