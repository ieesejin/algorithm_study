# https://www.acmicpc.net/problem/15681


from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def makeTree(currentNode, parent):
    for Node in connect[currentNode]:
        if Node != parent:
            child[currentNode].append(Node)
            parentList[Node] = currentNode
            makeTree(Node, currentNode)


def countSubTreeNodes(currentNode):
    size[currentNode] = 1
    for Node in child[currentNode]:
        countSubTreeNodes(Node)
        size[currentNode] += size[Node]


N, R, Q = map(int, input().split())

connect = defaultdict(list)
for i in range(N-1):
    U, V = map(int, input().split())
    connect[U].append(V)
    connect[V].append(U)

child = [[] for _ in range(N+1)]
parentList = [0 for _ in range(N+1)]
size = [0 for _ in range(N+1)]

makeTree(R, -1)
countSubTreeNodes(R)

for i in range(Q):
    q = int(input())
    print(size[q])
