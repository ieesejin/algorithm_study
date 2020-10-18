# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    user = dict()
    actCount = 0

    for idx, rec in enumerate(record):
        rec = rec.split(" ")
        if rec[0] == 'Enter' or rec[0] == 'Leave':
            actCount += 1

        if not rec[1] in user:
            user[rec[1]] = [rec[2], [(rec[0], idx)]]
        else:
            if rec[0] == 'Change':
                user[rec[1]][0] = rec[2]
            elif rec[0] == 'Enter':
                user[rec[1]][0] = rec[2]
                user[rec[1]][1].append((rec[0], idx))
            elif rec[0] == 'Leave':
                user[rec[1]][1].append((rec[0], idx))

    answer = ['' for _ in range(actCount)]
    for nickName, idxs in user.values():
        for act, idx in idxs:
            if act == 'Enter':
                answer[idx] = nickName + '님이 들어왔습니다.'
            if act == 'Leave':
                answer[idx] = nickName + '님이 나갔습니다.'

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
