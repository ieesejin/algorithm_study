# https://www.acmicpc.net/problem/10815


import sys
input = sys.stdin.readline
import bisect


N = int(input())
cards = sorted(list(map(int, input().split())))

M = int(input())
nums = list(map(int, input().split()))

answer = []
for num in nums:
    idx = bisect.bisect_left(cards, num)
    if idx == len(cards):
        answer.append(0)
    elif cards[idx] == num:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
