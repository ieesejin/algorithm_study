# https://www.acmicpc.net/problem/2805


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
trees = list(map(int, input().split()))
s, e = 1, max(trees)


def cuttingSum():
    total = 0
    for tree in trees:
        if tree > m:
            total += tree - m
    return total


while s <= e:
    m = (s+e) // 2
    total = cuttingSum()
    if total >= M:
        s = m + 1
    else:
        e = m - 1

print(e)
