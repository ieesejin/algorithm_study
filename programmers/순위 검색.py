# https://programmers.co.kr/learn/courses/30/lessons/72412


# 정확성 테스트만 통과
# def solution(info, query):
#     answer = []
#     for q in query:
#         q = q.replace("and", "")
#         q = q.replace("  ", " ")
#         q = q.split(" ")
#         count = 0
#         for i in info:
#             i = i.split()
#             for idx in range(len(q)-1):
#                 if q[idx] == '-':
#                     continue
#                 if q[idx] != i[idx]:
#                     break
#             else:
#                 if int(q[-1]) <= int(i[-1]):
#                     count += 1

#         answer.append(count)

#     return answer

# 정확성, 효율성 모두 통과
from itertools import combinations
import bisect # 이진탐색 라이브러리


def solution(info, query):
    answer = []
    info_dict = {}
    for i in info:
        data = i.split(" ")
        conditions = data[:-1]
        score = int(data[-1])

        # info에서 조합할 수 있는 모든 조합에 대해서 key, value = 조합, 점수 로 딕셔너리를 만듬
        # 점수는 조합에 대해 여러개가 될 수 있으므로 리스트 형태를 가짐
        for j in range(5):
            for comb in combinations(conditions, j):
                key = ''.join(comb)
                if key not in info_dict:
                    info_dict[key] = [score]
                else:
                    info_dict[key].append(score)

    # 이진탐색을 사용하기 위해 value(점수리스트)를 오름차순 정렬
    for value in info_dict.values():
        value.sort()

    for q in query:
        q = q.replace("and ", "")
        q = q.replace("-", "")
        data = q.split(" ")
        q_conditions = ''.join(data[:-1])
        q_score = int(data[-1])

        # 이진탐색: query의 score보다 큰 값 점수들의 갯수를 찾으면 되므로 dictionary의 value값 중 큰 값의 갯수만큼 answer에 넣으면 됨.
        # if q_conditions in info_dict:
        #     scores = info_dict[q_conditions]
        #     if len(scores) > 0:
        #         start, end = 0, len(scores)
        #         while end > start:
        #             mid = (start + end) // 2
        #             if scores[mid] >= q_score:
        #                 end = mid
        #             else:
        #                 start = mid + 1
        #         answer.append(len(scores) - start)
        # else:
        #     answer.append(0)

        # 이진탐색 라이브러리 사용
        if q_conditions in info_dict:
            idx = bisect.bisect_left(info_dict[q_conditions], q_score)
            answer.append(len(info_dict[q_conditions]) - idx)
        else:
            answer.append(0)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
# expected result: [1, 1, 1, 1, 2, 4]
