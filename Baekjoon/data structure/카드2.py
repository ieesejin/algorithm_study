# https://www.acmicpc.net/problem/2164


from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
q = deque([_+1 for _ in range(N)])

while len(q) != 1:
    q.popleft()
    if len(q) == 1:
        break
    q.append(q.popleft())

print(q[0])
