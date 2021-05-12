# https://www.acmicpc.net/problem/2417

import math

n = int(input())
answer = math.sqrt(n)
if answer - int(answer) > 0:
    print(int(answer)+1)

elif answer - int(answer) == 0:
    print(int(answer))

# 이분탐색
# n = int(input())
# s, e = 0, int((2**63)**0.5)+1
# res = 0
# while s <= e:
#     m = (s+e)//2
#     if m**2 >= n:
#         res = m
#         e = m-1
#     else:
#         s = m+1
# print(res)