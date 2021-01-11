# https://programmers.co.kr/learn/courses/30/lessons/49993


def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        idx = []
        for j in skill:
            if j in i:
                idx.append(i.index(j))
            else:
                idx.append(27)

        if idx == sorted(idx): # If it changes when sorted, the skill order is wrong.
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
