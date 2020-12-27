# https://programmers.co.kr/learn/courses/30/lessons/62048


# calculate gcd with width and height
def getGcd(w, h):
    if w < h:
        w, h = h, w

    while h != 0:
        w, h = h, w % h

    return w


def solution(w, h):
    gcd = getGcd(w, h)
    cuttedBlock = w / gcd + h / gcd - 1 # cutted block from the same pattern

    answer = w * h - gcd * (cuttedBlock) # blocks - cutted block

    return answer


print(solution(8, 12)) # expected answer: 96 - 16 = 80
