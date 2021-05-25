# https://www.acmicpc.net/problem/11720


import sys
input = sys.stdin.readline


N = int(input())
nums = list(map(int, list(input().rstrip())))
print(sum(nums))
