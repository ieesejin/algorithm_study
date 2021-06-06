# https://www.acmicpc.net/problem/1110


import sys
input = sys.stdin.readline


N = int(input())
new_N = N
cycle = 0
while True:
    a, b = divmod(new_N, 10)
    new_N = int(str(b) + str((a + b) % 10))
    cycle += 1
    if new_N == N:
        print(cycle)
        break
