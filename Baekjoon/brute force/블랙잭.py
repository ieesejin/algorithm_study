# https://www.acmicpc.net/problem/2798


from itertools import combinations


N, M = map(int, input().split())

cards = list(map(int, input().split()))
combs = combinations(cards, 3)

nearest = -1
for comb in combs:
    sum_comb = sum(comb)
    if sum_comb <= M:
        nearest = max(sum_comb, nearest)

print(nearest)
