# https://programmers.co.kr/learn/courses/30/lessons/42860


def solution(name):
    answer = 0
    count_A = 0
    A_li = []
    idx = 0
    for i in range(len(name)):
        if name[i] == 'A':
            count_A += 1
            idx = i
        else:
            A_li.append((count_A, idx - count_A + 1))
            count_A = 0
            continue
        A_li.append((count_A, idx - count_A + 1))

    A_length, A_idx = max(A_li, key=lambda x: x[0])

    for i in name:
        if i <= 'N':
            answer += ord(i) - ord('A')
        else:
            answer += 26 - (ord(i) - ord('A'))

    if 'A' not in name:
        answer += len(name) - 1
        return answer

    if A_length >= A_idx:
        answer += len(name) - 1 - (A_length + 1) + A_idx

    else:
        answer += len(name) - 1

    return answer


print(solution("JEROEN")) # expected result: 56
