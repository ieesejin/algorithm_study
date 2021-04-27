# https://www.acmicpc.net/problem/9934


import sys
input = sys.stdin.readline


K = int(input())
tree = [list(map(int, input().split()))]

while True:
    if not tree[0]:
        break

    temp = []
    for t in tree:
        center = len(t) // 2
        root = t[center]
        l_child = t[:center]
        r_child = t[center + 1:]
        temp.append(l_child)
        temp.append(r_child)
        print(root, end=' ')
    print()
    tree = temp
