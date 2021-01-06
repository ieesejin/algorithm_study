# https://programmers.co.kr/learn/courses/30/lessons/43165


def solution(numbers, target): # BFS
    results = [0]
    for number in numbers:
        temp = []
        for result in results:
            temp.append(result + number)
            temp.append(result - number)
        results = temp # Initialize the list by adding and subtracting number.

    return results.count(target)


def solution2(numbers, target): # DFS
    def dfs(i, numbers, target, total_sum):
        result = 0

        if i == len(numbers):
            if total_sum == target:
                return 1 # count
            else:
                return 0

        result += dfs(i + 1, numbers, target, total_sum + numbers[i])
        result += dfs(i + 1, numbers, target, total_sum - numbers[i])

        return result

    answer = dfs(0, numbers, target, 0) # start dfs

    return answer


print(solution([1, 1, 1, 1, 1], 3)) # expected value: 5
print(solution([1, 1, 1, 1, 1], 3)) # expected value: 5

# -1 + 1 + 1 + 1 + 1
# +1 - 1 + 1 + 1 + 1
# +1 + 1 - 1 + 1 + 1
# +1 + 1 + 1 - 1 + 1
# +1 + 1 + 1 + 1 - 1
