# https://www.acmicpc.net/problem/2609


import sys
input = sys.stdin.readline


num1, num2 = map(int, input().split())


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(num1, num2))
print(lcm(num1, num2))