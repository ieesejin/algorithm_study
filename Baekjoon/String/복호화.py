# https://www.acmicpc.net/problem/9046


from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    str1 = input().rstrip()
    str1 = str1.replace(" ", '')
    counter = Counter(str1)
    most_counter = counter.most_common()

    if len(most_counter) > 1 and most_counter[0][1] == most_counter[1][1]:
        print('?')
    else:
        print(most_counter[0][0])
