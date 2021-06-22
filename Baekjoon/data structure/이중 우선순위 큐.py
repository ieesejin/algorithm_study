# https://www.acmicpc.net/problem/7662


import heapq
import sys
input = sys.stdin.readline


q = []
T = int(input())

for test_case in range(T):
    k = int(input())
    min_hq, max_hq = [], []
    count = dict()
    for i in range(k):
        c, n = input().split(" ")
        n = int(n)
        if c == 'I':
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            heapq.heappush(min_hq, n)
            heapq.heappush(max_hq, -n)
        elif c == 'D':
            if n == -1:
                while min_hq:
                    min_pop = heapq.heappop(min_hq)
                    if min_pop in count and count[min_pop] > 0:
                        count[min_pop] -= 1
                        if not count[min_pop]:
                            del count[min_pop]
                        break
            elif n == 1:
                while max_hq:
                    max_pop = -heapq.heappop(max_hq)
                    if max_pop in count and count[max_pop] > 0:
                        count[max_pop] -= 1
                        if not count[max_pop]:
                            del count[max_pop]
                        break

    if count:
        sorted_items = sorted(count.items())
        print("{} {}".format(sorted_items[-1][0], sorted_items[0][0]))
    else:
        print("EMPTY")
