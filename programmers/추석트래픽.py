time_table = dict()

def time2sec(line):
    date, time, during = line.split()
    hour, minute, sec = time.split(':')
    end = int(hour) * 3600 + int(minute) * 60 + float(sec)
    during = float(during[:-1])

    # 기간으로 세는 것이 아닌 시간 당시로 세기 위해서 모든 길이를 왼쪽으로 1초씩 당겨줌
    # 0.0001 은 start와 end 가 겹치는 것을 처리
    start = end - during + 0.001 - 0.9991
    return start, end


def dup(sec):
    if sec not in time_table.keys():
        return sec
    else:
        return dup(sec + 0.000000001) # 중복이 2000개가 최대기 때문에 소수점을 4개 더 추가하면 겹치지 않음


def solution(lines):
    number = 0
    for line in lines:
        start, end = time2sec(line)
        time_table[dup(start)] = number
        time_table[dup(end)] = number
        number += 1

    history = []
    state = [0] * len(lines) # 0은 트래픽 꺼져있음, 1은 트래픽이 들어온 상황

    for time in sorted(time_table.keys()):
        number = time_table[time]
        if state[number] == 1:
            state[number] = 0
        elif state[number] == 0:
            state[number] = 1

        history.append(state.count(1)) # 시간이 지날때마다 1이 켜져있는 갯수를 기록

    return max(history) # 기록 중 최댓값 출력