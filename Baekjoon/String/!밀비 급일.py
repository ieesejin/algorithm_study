# https://www.acmicpc.net/problem/11365


import sys
input = sys.stdin.readline


stack = []
while True:
    line = input().rstrip()
    if line == 'END':
        break

    line = list(line)
    while line:
        print(line.pop(), end="")

    print()
