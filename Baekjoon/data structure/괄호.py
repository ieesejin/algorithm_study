# https://www.acmicpc.net/problem/9012


import sys
from collections import deque
input = sys.stdin.readline

# solve with counting (
#
# T = int(input())
#
# for test_case in range(T):
#     case = deque(list(input()))
#     left = 0
#     answer = "YES"
#     while case:
#         p = case.popleft()
#         if p == "(":
#             left += 1
#         elif p == ")":
#             left -= 1
#         if left < 0:
#             answer = "NO"
#             break
#
#     if left:
#         answer = "NO"
#
#     print(answer)


# solve with stack
T = int(input())

for test_case in range(T):
    case = list(input().rstrip())
    q = deque(case)
    stack = []
    while q:
        p = q.popleft()
        if stack:
            if p == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(p)
        else:
            stack.append(p)

    if stack:
        print("NO")
    else:
        print("YES")
