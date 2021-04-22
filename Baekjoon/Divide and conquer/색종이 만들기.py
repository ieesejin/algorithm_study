# https://www.acmicpc.net/problem/2630


def check(b):
    res = 0
    for row in b:
        for i in range(len(b)):
            if row[i] == 1:
                res += 1

    if res == len(b)**2 or res == 0:
        return True

    return False


def divide(b, n):
    global one
    global zero

    if n == 1 or check(b):
        if b[0][0] == 0:
            zero += 1
        if b[0][0] == 1:
            one += 1
        return

    first_b = []
    second_b = []
    third_b = []
    forth_b = []
    for row in range(n//2):
        first_b.append(b[:n//2][row][:n//2])
        second_b.append(b[:n//2][row][n//2:])
        third_b.append(b[n//2:][row][:n//2])
        forth_b.append(b[n//2:][row][n//2:])

    divide(first_b, n//2)
    divide(second_b, n // 2)
    divide(third_b, n // 2)
    divide(forth_b, n // 2)


N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

one = 0
zero = 0

divide(board, N)

print(zero)
print(one)
