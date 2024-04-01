import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def preorder(ins, ine, posts, poste):
    if ins > ine or posts > poste:
        return

    parents = postorder[poste]
    print(parents, end=' ')

    left = graph[parents] - ins
    right = ine - graph[parents]

    preorder(ins, ins + left - 1, posts, posts + left - 1)
    preorder(ine - right + 1, ine, poste - right, poste - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

graph = [0] * (n + 1)
for i in range(n):
    graph[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)
