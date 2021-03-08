# https://programmers.co.kr/learn/courses/30/lessons/72415?language=python3


from itertools import permutations
from collections import deque


def solution(board, r, c):
    cards = {} # 카드 짝 끼리 저장
    for y in range(4):
        for x in range(4):
            if board[y][x] != 0:
                card = board[y][x]
                if card not in cards.keys():ㅎ
                    cards[card] = [(y, x)]
                else:
                    cards[card].append((y, x))

    perms = permutations(list(cards.keys())) # 카드를 뽑을 순서 조합
    answer = 10000
    for perm in perms: # 모든 조합에 대해 최솟값을 찾음
        res = cal_min(board, cards, perm, (r, c))
        answer = min(res, answer)

    return answer


def bfs(board, s, e): # s 위치에서 e 위치까지 가는 최솟값
    q = deque()

    s_y, s_x = s[0], s[1]
    e_y, e_x = e[0], e[1]

    q.append((s_y, s_x, 0))

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    check = {(s_y, s_x)}

    while q:
        y, x, count = q.popleft()

        if y == e_y and x == e_x: # e 위치에 도착
            board[y][x] = 0
            return count

        for dy, dx in d: # 동, 서, 남, 북 방향으로 이동
            cur_y, cur_x = y, x # ctrl + 방향키를 사용하기 위해 시작 위치 임시 저장
            if 0 <= y + dy < 4 and 0 <= x + dx < 4 and (y + dy, x + dx) not in check: # 방향키로 한칸 이동하는 경우
                q.append((y + dy, x + dx, count + 1))
                check.add((y + dy, x + dx))

            while 0 <= cur_y + dy < 4 and 0 <= cur_x + dx < 4: # ctrl + 방향키로 카드를 만나거나 board 끝까지 이동 하는 경우
                cur_y += dy
                cur_x += dx
                if board[cur_y][cur_x] != 0:
                    break

            if (cur_y, cur_x) not in check:
                q.append((cur_y, cur_x, count + 1))
                check.add((cur_y, cur_x))


# 조합에 대해서 최솟값을 구함
# 한 조합당 2**카드종류수 만큼의 경우가 나옴
# recursive를 이용해 계산
def cal_min(board, cards, perm, s):
    if not perm: # recursive 탈출 조건: 카드 종류를 다 썼을 경우
        return 0

    answer = 10000

    p = perm[0] # 먼저 사용할 카드
    perm = perm[1:] # 조합에서 사용한 카드를 뺌

    # a, b: 현재 위치에서 한 종류의 카드에 대해서 이동할 수 있는 2가지 경우
    a = bfs(board, s, cards[p][0]) + bfs(board, cards[p][0], cards[p][1]) + cal_min(board, cards, perm, cards[p][1])
    board[cards[p][0][0]][cards[p][0][1]] = p # board를 재사용해야 하므로 bfs 함수에서 지운 카드 값을 다시 채워줌
    board[cards[p][1][0]][cards[p][1][1]] = p
    b = bfs(board, s, cards[p][1]) + bfs(board, cards[p][1], cards[p][0]) + cal_min(board, cards, perm, cards[p][0])
    board[cards[p][0][0]][cards[p][0][1]] = p
    board[cards[p][1][0]][cards[p][1][1]] = p

    answer = min(a, b) + 2 # enter 두번 입력하는 것을 고려

    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)) # expected result: 14
