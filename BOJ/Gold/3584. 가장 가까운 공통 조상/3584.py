import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def LCA(node, parent):
    depth[node] = depth[parent] + 1
    dp[node][0] = parent

    for i in range(1, max_level + 1):
        tmp = dp[node][i - 1]
        dp[node][i] = dp[tmp][i - 1]

    for next in graph[node]:
        if next != parent:
            LCA(next, node)


for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        check[b] = 1
        graph[a].append(b)
        graph[b].append(a)

    max_level = int(math.log2(n))
    dp = [[0] * (max_level + 1) for _ in range(n + 1)]
    depth = [0] * (n + 1)
    depth[0] = -1
    root = [i for i in range(1, n + 1) if check[i] == 0][0]
    LCA(root, 0)

    a, b = map(int, input().split())
    if depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a, b = b, a

        for i in range(max_level, -1, -1):
            if depth[a] <= depth[dp[b][i]]:
                b = dp[b][i]

    result = a
    if a != b:
        for i in range(max_level, -1, -1):
            if dp[a][i] != dp[b][i]:
                a, b = dp[a][i], dp[b][i]
            result = dp[a][i]

    print(result)
