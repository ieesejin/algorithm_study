# https://github.com/tony9402/baekjoon/tree/main/brute_force


import sys
input = sys.stdin.readline


N, K = map(int, input().split())

h, m, s = 0, 0, 0
K = str(K)
count = 0

while True:
    if K in str(h).zfill(2) or K in str(m).zfill(2) or K in str(s).zfill(2):
        count += 1

    if h == N and m == 59 and s == 59:
        break

    s += 1

    if s == 60:
        s -= 60
        m += 1

    if m == 60:
        m -= 60
        h += 1

print(count)
