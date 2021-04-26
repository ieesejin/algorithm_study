# https://www.acmicpc.net/problem/14425


N, M = map(int, input().split())

str1 = [input() for _ in range(N)]
str2 = [input() for _ in range(M)]

count = 0
for s in str2:
    if s in str1:
        count += 1

print(count)
