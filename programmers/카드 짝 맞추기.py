# https://programmers.co.kr/learn/courses/30/lessons/72415?language=python3


from collections import deque


def solution(board, r, c):
    cards = {}
    for y in range(4):
        for x in range(4):
            if board[y][x] != 0:
                card = board[y][x]
                if card not in cards.keys():
                    cards[card] = [(y, x)]
                else:
                    cards[card].append((y, x))

    return cal_min(board, cards, list(cards.keys()), (r, c))


def bfs(board, s, e):
    q = deque()

    s_y, s_x = s[0], s[1]
    e_y, e_x = e[0], e[1]

    q.append((s_y, s_x, 0))

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    check = {(s_y, s_x)}

    while q:
        y, x, count = q.popleft()

        if y == e_y and x == e_x:
            board[y][x] = 0
            return count

        for dy, dx in d:
            cur_y, cur_x = y, x
            if 0 <= y + dy < 4 and 0 <= x + dx < 4 and (y + dy, x + dx) not in check:
                q.append((y + dy, x + dx, count + 1))
                check.add((y + dy, x + dx))

            while 0 <= cur_y + dy < 4 and 0 <= cur_x + dx < 4:
                cur_y += dy
                cur_x += dx
                if board[cur_y][cur_x] != 0:
                    break

            if (cur_y, cur_x) not in check:
                q.append((cur_y, cur_x, count + 1))
                check.add((cur_y, cur_x))


def cal_min(board, cards, keys, s):
    if not keys:
        return 0

    answer = 10000

    for i in range(len(keys)):
        a = bfs(board, s, cards[keys[i]][0]) + bfs(board, cards[keys[i]][0], cards[keys[i]][1]) + cal_min(board, cards, keys[:i] + keys[i + 1:], cards[keys[i]][1])
        board[cards[keys[i]][0][0]][cards[keys[i]][0][1]] = keys[i]
        board[cards[keys[i]][1][0]][cards[keys[i]][1][1]] = keys[i]

        b = bfs(board, s, cards[keys[i]][1]) + bfs(board, cards[keys[i]][1], cards[keys[i]][0]) + cal_min(board, cards, keys[:i] + keys[i + 1:], cards[keys[i]][0])
        board[cards[keys[i]][0][0]][cards[keys[i]][0][1]] = keys[i]
        board[cards[keys[i]][1][0]][cards[keys[i]][1][1]] = keys[i]

        answer = min(min(a, b) + 2, answer)

    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)) # expected result: 14
