def combinations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        element = arr[i]
        rest_arr = arr[i+1:]
        for C in combinations(rest_arr, n-1):
            result.append([element] + C)

    return result


print(combinations([1, 2, 3, 4, 5], 3))
