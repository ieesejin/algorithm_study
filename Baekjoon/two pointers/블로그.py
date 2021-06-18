# https://www.acmicpc.net/problem/21921


import sys
input = sys.stdin.readline


N, X = map(int, input().split())
visitor = list(map(int, input().split()))

count_max = 1

sum_visit = sum(visitor[:X])
max_visit = sum_visit
for i in range(X, N):
    sum_visit += visitor[i]
    sum_visit -= visitor[i-X]
    if sum_visit > max_visit:
        max_visit = sum_visit
        count_max = 1
    elif sum_visit == max_visit:
        count_max += 1

if max_visit:
    print(max_visit)
    print(count_max)
else:
    print("SAD")

