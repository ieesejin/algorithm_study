# https://www.acmicpc.net/problem/14929

n = int(input())
nums = list(map(int, input().split()))

if n < 2:
    print(0)

else:
    sum_ = nums[0] * nums[1]
    temp = nums[0] + nums[1]

    for i in range(2, len(nums)):
        sum_ += temp * nums[i]
        temp += nums[i]

    print(sum_)
