# https://www.acmicpc.net/problem/4358


import sys
from collections import Counter
input = sys.stdin.readline


species = []
while True:
    s = input().rstrip()
    if s == "":
        break
    species.append(s)

counter = Counter(species)
keys = sorted(list(counter.keys()))
length = len(species)

for key in keys:
    print("%s %.4f" % (key, ((int(counter[key]) / length) * 100)))
