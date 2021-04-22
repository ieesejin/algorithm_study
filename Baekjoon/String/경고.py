# https://www.acmicpc.net/problem/3029


cur_time_h, cur_time_m, cur_time_s = map(int, input().split(":"))
boom_time_h, boom_time_m, boom_time_s = map(int, input().split(":"))

wait_time_h = 23 - cur_time_h
wait_time_m = 59 - cur_time_m
wait_time_s = 59 - cur_time_s

wait_time_h += boom_time_h
wait_time_m += boom_time_m
wait_time_s += boom_time_s + 1

if wait_time_s >= 60:
    wait_time_m += 1
    wait_time_s -= 60

if wait_time_m >= 60:
    wait_time_h += 1
    wait_time_m -= 60

if wait_time_h >= 24:
    wait_time_h -= 24

if wait_time_h == 0 and wait_time_m == 0 and wait_time_s == 0:
    wait_time_h = 24

print(str(wait_time_h).zfill(2) + ":" + str(wait_time_m).zfill(2) + ":" + str(wait_time_s).zfill(2))
