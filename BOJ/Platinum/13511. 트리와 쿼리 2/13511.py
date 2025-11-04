import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def init(now, d):
    visited[now] = 1
    depth[now] = d
    for node, dist in graph[now]:
        if visited[node]:
            continue

        parents[node][0] = now
        dists[node] = dists[now] + dist
        init(node, d + 1)


def connect():
    for i in range(1, m):
        for now in range(1, n + 1):
            parent = parents[now][i - 1]
            parents[now][i] = parents[parent][i - 1]
            if not parents[parent][i - 1]:
                continue


def LCA(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    for i in range(m - 1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            y = parents[y][i]

    if x == y:
        return x

    for i in range(m - 1, - 1, -1):
        if parents[x][i] == parents[y][i]:
            continue

        x = parents[x][i]
        y = parents[y][i]

    return parents[x][0]


def get_dist(x, y):
    lca = LCA(x, y)
    return dists[x] + dists[y] - 2 * dists[lca]


def find(node, k):
    for i in range(m):
        if k & (1 << i):
            node = parents[node][i]

    return node


def kth_node(x, y, k):
    lca = LCA(x, y)
    dx, dy = depth[x] - depth[lca], depth[y] - depth[lca]
    if k <= dx + 1:
        return find(x, k - 1)

    else:
        k = dx + dy + 1 - k
        return find(y, k)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

m = int(math.log2(n)) + 1
parents = [[0] * m for _ in range(n + 1)]
dists = [0] * (n + 1)
visited = [0] * (n + 1)
depth = [0] * (n + 1)
init(1, 0)
connect()

queries = [list(map(int, input().split())) for _ in range(int(input()))]
for query in queries:
    if query[0] == 1:
        print(get_dist(*query[1:]))

    else:
        print(kth_node(*query[1:]))
