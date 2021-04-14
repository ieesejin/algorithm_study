# https://www.acmicpc.net/problem/10870


n = int(input())

fiv = [0 for _ in range(21)]
fiv[0] = 0
fiv[1] = 1

for i in range(2, 21):
    fiv[i] = fiv[i-1] + fiv[i-2]

print(fiv[n])
