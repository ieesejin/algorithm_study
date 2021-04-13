# https://www.acmicpc.net/problem/1158


from collections import deque
import sys


N, K = map(int, sys.stdin.readline().split())


q = deque([x for x in range(1, N+1)])
out = []

idx = 0
while q:
    person = q.popleft()
    idx += 1
    if idx % K == 0:
        out.append(str(person))
    else:
        q.append(person)

print("<" + ', '.join(out) + ">")

#
# while person:
#     idx += K-1
#     idx = idx % len(person)
#     answer.append(str(person.pop(idx)))
