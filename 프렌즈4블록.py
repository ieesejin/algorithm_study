# https://programmers.co.kr/learn/courses/30/lessons/17679


def find4Block(m, n, board):
    char = ['R', 'M', 'A', 'F', 'N', 'T', 'J', 'C']
    erasePoint = []
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] in char and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                erasePoint.append((i, j))

    for y, x in erasePoint:
        board[y][x] = '0'
        board[y+1][x] = '0'
        board[y][x+1] = '0'
        board[y+1][x+1] = '0'

    return board


def dropBlock(m, n, board):
    for i in range(m-1, -1, -1):
        for j in range(n):
            if board[i][j] == '0':


def solution(m, n, board):
    answer = 0
    board = [list(line) for line in board]
    find4Block(m, n, board)

    return answer


print(find4Block(6, 6, [list(line) for line in ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]))
