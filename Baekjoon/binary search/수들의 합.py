# https://www.acmicpc.net/problem/1789


S = int(input())
n = 1
while n * (n + 1) / 2 <= S:
    n += 1

print(n - 1)


# import sys
#
# S = int(sys.stdin.readline().rstrip())
#
# start = 1;
# end = S
# answer=0
#
# while start <= end:
#     mid = (start + end) // 2
#     if mid * (mid + 1) // 2 <= S:
#         answer = mid
#         start = mid + 1
#     else:
#         end = mid - 1
#
# print(answer)