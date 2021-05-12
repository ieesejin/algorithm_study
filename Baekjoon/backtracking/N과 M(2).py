# https://www.acmicpc.net/problem/15650

from itertools import combinations


N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

combs = list(map(list, combinations(nums, M)))

for comb in combs:
    print(*comb)


# 백트래킹
# import sys
#
# input = sys.stdin.readline
#
#
# def backtracking(list, start):
#
#     global answer
#
#     if len(list) == M:
#         answer.append(list)
#         return
#
#     for num in range(start, N + 1):
#         if visited[num] != 1:
#
#             visited[num] = 1
#             tmp = list[:]
#             tmp.append(num)
#
#             backtracking(tmp, num)
#
#             visited[num] = 0
#
#
# N, M = map(int, input().split())
#
# visited = [0] * (N + 1)
# answer = []
#
# backtracking([], 1)
#
# for lst in answer:
#     print(' '.join(map(str, lst)))