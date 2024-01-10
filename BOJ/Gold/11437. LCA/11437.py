import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))


def LCA(here, parent):
    depth[here] = depth[parent] + 1
    dp[here][0] = parent

    for i in range(1, max_level + 1):
        tmp = dp[here][i - 1]
        dp[here][i] = dp[tmp][i - 1]

    for node in graph[here]:
        if node != parent:
            LCA(node, here)


n = int(input())
max_level = int(math.log2(n))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n + 1)
depth[0] = -1
dp = [[0] * 20 for _ in range(n + 1)]

LCA(1, 0)

m = int(input())
for _ in range(m):
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
