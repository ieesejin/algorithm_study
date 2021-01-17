# https://programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    if len(s) < 3:
        return len(s)

    answer = len(s)
    split = int(len(s) / 2)

    for i in range(1, split + 1):
        interval = int(len(s) / i)
        count = 1
        result = ""

        for j in range(interval):
            pre_word = s[i * j:i * (j + 1)]
            next_word = s[i * (j + 1):i * (j + 2)]

            if pre_word == next_word:
                count += 1

            if pre_word != next_word:
                if count > 1:
                    result = result + str(count) + pre_word
                    count = 1
                else:
                    result += pre_word

        remain = len(s) % i
        answer = min(answer, len(result) + remain)

    return answer


print(solution("aabbaccc")) # expected result: 7
