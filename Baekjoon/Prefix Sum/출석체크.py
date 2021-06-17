# https://www.acmicpc.net/problem/20438


import sys
input = sys.stdin.readline


N, K, Q, M = map(int, input().split())

sleeps = list(map(int, input().split()))
codes = list(map(int, input().split()))

students = [1 for _ in range(N+3)]
students[0] = 0
students[1] = 0
students[2] = 0

for code in codes:
    if code in sleeps:
        continue
    i = 2
    temp = code
    while temp <= N+2:
        if temp not in sleeps:
            students[temp] = 0
        temp = code * i
        i += 1

for i in range(1, len(students)):
    students[i] += students[i-1]

for i in range(M):
    S, E = map(int, input().split())
    print(students[E] - students[S-1])
