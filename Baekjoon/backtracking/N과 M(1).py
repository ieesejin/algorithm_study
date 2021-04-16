# https://www.acmicpc.net/problem/15649


from itertools import permutations


N, M = map(int, input().split())
li = [i+1 for i in range(N)]
perms = permutations(li, M)
for perm in perms:
    print(' '.join(map(str, perm)))


# def backtracking(arr):
#
#     global answer
#
#     if len(arr) == M:
#         answer.append(arr)
#         return
#
#     for i in range(1, N + 1):
#
#         if visited[i] != 1:
#             visited[i] = 1
#             temp = arr[:]
#             temp.append(i)
#             backtracking(temp)
#             visited[i] = 0
#
#
# N, M = map(int, input().split())
#
# visited = [0] * (N + 1)
#
# answer = []
# backtracking([])
#
# print(answer)
