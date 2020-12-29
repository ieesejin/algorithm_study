# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


# check the number is prime.
def isPrime(number):
    res = False

    if number < 2:
        return res

    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return res

    return True


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers) + 1):
        p = set()
        for j in permutations(numbers, i): # find all combinations.
            p.add(j)

        for k in p: # If the first digit is 0, it is redundant, so use set to remove it.
            num = int(''.join(k))
            if isPrime(num):
                answer.add(num)

    return len(answer)


print(solution("17")) # expected result: [7, 17, 71] => 3
