import sys
input = sys.stdin.readline


class Node:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right


def preorder(X):
    print(X.node, end='')

    if X.left != '.':
        preorder(graph[X.left])

    if X.right != '.':
        preorder(graph[X.right])


def inorder(X):
    if X.left != '.':
        inorder(graph[X.left])

    print(X.node, end='')

    if X.right != '.':
        inorder(graph[X.right])


def postorder(X):
    if X.left != '.':
        postorder(graph[X.left])

    if X.right != '.':
        postorder(graph[X.right])

    print(X.node, end='')


n = int(input())
graph = dict()

for _ in range(n):
    x, y, z = input().split()
    graph[x] = Node(x, y, z)

preorder(graph['A'])
print()
inorder(graph['A'])
print()
postorder(graph['A'])
