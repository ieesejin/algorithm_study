# https://programmers.co.kr/learn/courses/30/lessons/42587


def solution(priorities, location):
    answer = 0
    idx = list(range(0, len(priorities)))
    idx_priorities = list(zip(priorities, idx))
    while len(idx_priorities) != 0:
        if idx_priorities[0][0] < max(idx_priorities)[0]:
            idx_priorities.append(idx_priorities[0])
            idx_priorities.pop(0)
        elif idx_priorities[0][0] >= max(idx_priorities)[0]:
            answer += 1
            if idx_priorities[0][1] == location:
                return answer

            idx_priorities.pop(0)

    return answer


print(solution([2, 1, 3, 2], 2)) # expected result: 1
