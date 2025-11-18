import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def set_depth(now, dep):
    visited[now] = 1
    depth[now] = dep
    for node in graph[now]:
        if visited[node]:
            continue

        parents[node][0] = now
        dists[node][0] = 1
        set_depth(node, dep + 1)


def LCA(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    dist = 0
    for i in range(max_level - 1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            dist += dists[y][i]
            y = parents[y][i]

    if x == y:
        return dist

    for i in range(max_level - 1, -1, -1):
        if parents[x][i] == parents[y][i]:
            continue

        dist += dists[x][i]
        x = parents[x][i]

        dist += dists[y][i]
        y = parents[y][i]

    dist += dists[x][0] + dists[y][0]
    return dist


n = int(input())
max_level = int(math.log2(n)) + 1
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (n + 1)
dists = [[0] * (max_level) for _ in range(n + 1)]
parents = [[0] * (max_level) for _ in range(n + 1)]

visited = [0] * (n + 1)
set_depth(1, 0)

for i in range(1, max_level):
    for now in range(1, n + 1):
        parent = parents[now][i - 1]
        parents[now][i] = parents[parent][i - 1]
        if not parents[parent][i - 1]:
            continue

        dist = dists[now][i - 1]
        dists[now][i] = dist + dists[parent][i - 1]

result = 0
now = 1
for node in [int(input()) for _ in range(int(input()))]:
    result += LCA(now, node)
    now = node

print(result)
