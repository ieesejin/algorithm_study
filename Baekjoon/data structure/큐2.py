# https://www.acmicpc.net/problem/18258


from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
q = deque()

for i in range(N):
    c = list(input().split())
    if len(c) == 1:
        if c[0] == 'pop':
            if not q:
                print(-1)
            else:
                print(q.popleft())
        elif c[0] == 'size':
            print(len(q))
        elif c[0] == 'empty':
            if not q:
                print(1)
            else:
                print(0)
        elif c[0] == 'front':
            if not q:
                print(-1)
            else:
                print(q[0])
        elif c[0] == 'back':
            if not q:
                print(-1)
            else:
                print(q[-1])
    if len(c) == 2:
        q.append(int(c[1]))
