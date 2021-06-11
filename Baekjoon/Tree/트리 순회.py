# https://www.acmicpc.net/problem/1991


import sys
input = sys.stdin.readline


N = int(input())
tree = dict()
for i in range(N):
    temp = list(input().split())
    tree[temp[0]] = [temp[1], temp[2]]


def preorderTraversal(root):
    left, right = tree[root]
    order.append(root)
    if left != '.':
        preorderTraversal(left)
    if right != '.':
        preorderTraversal(right)


order = []
preorderTraversal('A')
print(''.join(order))


def inorderTraversal(root):
    left, right = tree[root]
    if left != '.':
        inorderTraversal(left)
    order.append(root)
    if right != '.':
        inorderTraversal(right)


order = []
inorderTraversal('A')
print(''.join(order))


def postorderTraversal(root):
    left, right = tree[root]
    if left != '.':
        postorderTraversal(left)
    if right != '.':
        postorderTraversal(right)
    order.append(root)


order = []
postorderTraversal('A')
print(''.join(order))
