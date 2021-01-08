# https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    answer = []
    count = 0
    zip_list = zip(progresses, speeds)

    while True:
        sum = [x + y for x, y in zip_list]

        if sum[count] >= 100:
            temp = 0
            while sum[count] >= 100:
                count += 1
                temp += 1
                if count == len(progresses):
                    break

            answer.append(temp)

        if count == len(progresses):
            break

        zip_list = zip(sum, speeds)

    return answer


print(solution([93, 30, 55], [1, 30, 5])) # expected result: [2, 1]
