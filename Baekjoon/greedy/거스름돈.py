# https://www.acmicpc.net/problem/14916


n = int(input())

x = n // 5
n = n - 5 * x

if x == 0 and n % 2 == 0:
    print(n // 2)

while x != 0:
    if n % 2 == 0:
        print(x + n // 2)
        break
    else:
        x -= 1
        n += 5

if x < 0 or n % 2 != 0:
    print(-1)
