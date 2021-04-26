def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i, element in enumerate(arr):
        for P in permutations(arr[:i] + arr[i+1:], n-1):
            result.append([element] + P)

    return result


print(permutations([1, 2, 3, 4, 5], 3))
