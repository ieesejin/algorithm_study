# https://programmers.co.kr/learn/courses/30/lessons/70130


from collections import Counter


def solution(a):
    answer = -1
    count = Counter(a)

    for key in count.keys():
        if count[key] <= answer: # 이미 최대값이 나온 경우
            continue
        count_set = 0
        idx = 0
        while idx < len(a) - 1:
            if (a[idx] != key and a[idx + 1] != key) or (a[idx] == a[idx + 1]): # 스타 수열이 안되는 조건
                idx += 1 # 한칸옆으로 해서 다시 확인
                continue
            count_set += 1
            idx += 2 # 셋을 이루었기 때문에 2칸
        answer = max(count_set, answer)

    if answer == -1:
        return 0

    return answer * 2 # 2개 원소 씩


print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0])) # expected result: 8
