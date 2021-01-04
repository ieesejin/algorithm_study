# https://programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    answer = 1
    closet = {} # initial dictionary
    for cloth, kind in clothes:
        if kind not in closet: # if key is not in dict
            closet[kind] = 1
        else:
            closet[kind] += 1

    for value in closet.values(): # Multiply the number of clothes for each kind.
        answer *= value + 1 # If you don't wear it, you have to add it.

    answer -= 1 # Excludes the case of not wearing all.

    return answer