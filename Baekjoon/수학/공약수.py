# https://www.acmicpc.net/problem/5618

# 최대공약수를 구해서 최대공약수의 약수를 출력하는 방법이 더 효율적이다.
# def gcd(a, b):
#     if b > a:
#         a, b = b, a
#     while b:
#         temp = a % b
#         a = b
#         a = temp
#     return abs(a)


import sys

n = sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))

cands = []
min_num = min(nums)
for i in range(1, int(min_num ** 0.5) + 1):
    if min_num % i == 0:
        cands.append(i)
        cands.append(int(min_num/i))

temp = []
for num in nums:
    if num == min_num:
        continue
    for cand in cands:
        if num % cand != 0:
            temp.append(cand)

answer = sorted([cand for cand in cands if cand not in temp])

for ans in sorted(list(set(answer))):
    print(ans)
