# https://programmers.co.kr/learn/courses/30/lessons/72414


def time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    return h * 3600 + m * 60 + s


def sec_to_time(sec):
    h, r = divmod(sec, 3600)
    m, s = divmod(r, 60)
    h = str(h).zfill(2) # '2' -> '02'
    m = str(m).zfill(2)
    s = str(s).zfill(2)

    return h + ":" + m + ":" + s


def solution(play_time, adv_time, logs):
    time_table = [0 for _ in range(time_to_sec(play_time) + 1)]
    for log in logs:
        start, end = log.split("-")
        start = time_to_sec(start)
        end = time_to_sec(end)
        # for i in range(start, end):
        #     time_table[i] += 1
        time_table[start] += 1 # 광고 시청자 시작을 1로 체크하고 끝나는 부분을 -1로 체크
        time_table[end] -= 1

    for i in range(1, len(time_table)): # 각 초별 시청자를 채워줌
        time_table[i] = time_table[i] + time_table[i - 1]

    adv_time = time_to_sec(adv_time)

    _sum = 0
    for j in range(adv_time): # 처음 0초부터 광고 시간만큼 동안의 시청자
        _sum += time_table[j]

    adv_start = 0
    max_sum = _sum
    for k in range(adv_time, len(time_table)): # 윈도우 크기를 똑같이 오른쪽으로 이동할때 오른쪽을 더하고 맨 왼쪽을 빼서 합을 갱신
        _sum += time_table[k]
        _sum -= time_table[k - adv_time]
        if max_sum < _sum:
            max_sum = _sum
            adv_start = k - adv_time + 1 # k는 광고 끝나는 시간이므로 시작시간을 계산

    return sec_to_time(adv_start)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:"
                                                                                                                            "02:30"])) # expected result: "01:30:59"