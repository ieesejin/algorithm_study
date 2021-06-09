# https://www.acmicpc.net/problem/2224


from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(start_node):
    visited = dict()
    visited[start_node] = 1
    stack = [start_node]
    res = []
    while stack:
        cur_node = stack.pop()
        for node in graph[cur_node]:
            if node not in visited:
                stack.append(node)
                visited[node] = 1
                res.append("{} => {}".format(start_node, node))

    return res


N = int(input())
graph = defaultdict(list)

for i in range(N):
    before, after = input().rstrip().split(" => ")
    graph[before].append(after)

answer = []
for key in list(graph.keys()):
    answer.extend(dfs(key))

answer.sort()

print(len(answer))
for ans in answer:
    print(ans)
