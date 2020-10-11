# https://programmers.co.kr/learn/courses/30/lessons/17678


def time2min(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)


def min2time(min):
    div, mod = divmod(min, 60)
    return "%02d:%02d" % (div, mod)


def shuttleTime(n, t, start="09:00"):
    shuttle = [time2min(start)]
    for i in range(n-1):
        shuttle.append(shuttle[-1] + t)

    return shuttle


def solution(n, t, m, timetable):
    answer = ''
    crewTime = sorted([time2min(time) for time in timetable])
    shuttle = shuttleTime(n, t)

    for i in range(n):
        count = 0
        if i == n-1:
            if len(crewTime) < m:  # 남은 인원이 넉넉해서 막차 타면 되는경우
                return min2time(shuttle[-1])

            else: # 남은 인원이 막차에 다 타지 못하는 경우
                for j in range(m):
                    if crewTime[j] <= shuttle[i]:
                        count += 1
                    else:
                        break
                if count == m:
                    return min2time(crewTime[j]-1)
                else:
                    return min2time(shuttle[i])

        # 셔틀에 되는 인원만큼 태워 보냄
        for l in range(m):
            if crewTime[0] <= shuttle[i]:
                crewTime.pop(0)
            else:
                break
