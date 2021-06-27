# https://www.acmicpc.net/problem/18222


import sys
input = sys.stdin.readline


def thueMorse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2:
        return 1 - thueMorse(n // 2)
    else:
        return thueMorse(n // 2)


k = int(input())
print(thueMorse(k-1))
