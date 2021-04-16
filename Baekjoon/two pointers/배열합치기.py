# https://www.acmicpc.net/problem/11728


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(' '.join(map(str, sorted(A+B)))) --> quick sort

idx_a, idx_b = 0, 0
answer = []
while True:
    if A[idx_a] >= B[idx_b]:
        answer.append(B[idx_b])
        idx_b += 1
    else:
        answer.append(A[idx_a])
        idx_a += 1

    if idx_a == len(A):
        answer.extend(B[idx_b:])
        break
    if idx_b == len(B):
        answer.extend(A[idx_a:])
        break

print(' '.join(map(str, answer)))
