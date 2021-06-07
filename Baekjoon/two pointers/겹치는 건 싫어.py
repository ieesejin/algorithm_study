# https://www.acmicpc.net/problem/20922


import sys
input = sys.stdin.readline


N, K = map(int, input().split())
nums = list(map(int, input().split()))
counter = dict()
left = 0
max_length = 0

for i in range(len(nums)):
    if nums[i] not in counter:
        counter[nums[i]] = 1
    else:
        counter[nums[i]] += 1

    if counter[nums[i]] > K:
        max_length = max(max_length, i-left)
        while True:
            if counter[nums[i]] <= K:
                break
            counter[nums[left]] -= 1
            left += 1

max_length = max(max_length, N - left)

print(max_length)
