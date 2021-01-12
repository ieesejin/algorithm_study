# https://programmers.co.kr/learn/courses/30/lessons/42584


def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        count = 0
        for j in range(i + 1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break

        answer.append(count)

    answer.append(0)

    return answer


print(solution([1, 2, 3, 2, 3])) # expected result: [4, 3, 1, 1, 0]
