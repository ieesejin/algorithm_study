# https://programmers.co.kr/learn/courses/30/lessons/72411


from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        comb_li = []
        for order in orders:
            for comb in combinations(order, i): # make combinations
                comb_li.append(''.join(sorted(comb))) # using sort --> "AC", "CA" same menu

        count = Counter(comb_li).most_common() # return most_common order list
        answer += [comb for comb, num in count if num > 1 and num == count[0][1]]
        answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])) # expected result: ["AC", "ACDE", "BCFG", "CDE"]
