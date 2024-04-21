import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def postorder(ins, ine, pres, pree):
    if ins > ine or pres > pree:
        return
    
    parent = preorder[pres]

    left = graph[parent] - ins
    right = ine - graph[parent]

    postorder(ins, ins + left - 1, pres + 1, pres + left)
    postorder(ine - right + 1, ine, pree - right + 1, pree)
    print(parent, end=' ')


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    graph = [0] * (n + 1)
    for i in range(n):
        graph[inorder[i]] = i

    postorder(0, n - 1, 0, n - 1)
    print()
