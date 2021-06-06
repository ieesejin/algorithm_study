# https://www.acmicpc.net/problem/20056


from collections import deque, defaultdict
import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

fireball = deque()
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r, c, m, s, d])

for i in range(K):
    pos = defaultdict(list)
    while fireball:
        fire = fireball.popleft()
        fr, fc, fm, fs, fd = fire
        fr = (fr + direction[fd][0]*fs) % N
        fc = (fc + direction[fd][1]*fs) % N
        pos[(fr, fc)].append([fm, fs, fd])

    for key in pos.keys():
        fr, fc = key
        length = len(pos[key])
        if length >= 2:
            sum_m = 0
            sum_v = 0
            odd = 0
            for fm, fs, fd in pos[key]:
                sum_m += fm
                sum_v += fs
                if fd % 2 == 1:
                    odd += 1

            if odd == 0 or odd == length:
                splash = [0, 2, 4, 6]
            else:
                splash = [1, 3, 5, 7]

            if sum_m // 5 > 0:
                for j in splash:
                    fireball.append([fr, fc, sum_m//5, sum_v//length, j])
        else:
            fm, fs, fd = pos[key][0]
            fireball.append([fr, fc, fm, fs, fd])

answer = 0
for fire in fireball:
    answer += fire[2]

print(answer)
