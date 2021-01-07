# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length # use list as a queue
    sec = 0
    while q:
        sec += 1
        q.pop(0) # popleft
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0)) # push
            else:
                q.append(0)

    return sec


print(solution(2, 10, [7, 4, 5, 6]))
