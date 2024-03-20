import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def set_depth(here, dep):
    visited[here] = 1
    depth[here] = dep

    for next, dist in graph[here]:
        if visited[next]:
            continue

        parents[next][0] = here
        lengths[next][0] = dist
        set_depth(next, dep + 1)


def connect():
    for i in range(1, MAX_LEVEL):
        for cur in range(1, n + 1):
            parent = parents[cur][i - 1]
            parents[cur][i] = parents[parent][i - 1]

            if parents[parent][i - 1] == 0:
                continue

            length = lengths[cur][i - 1]
            lengths[cur][i] = length + lengths[parent][i - 1]


def LCA(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    lsum = 0

    for i in range(MAX_LEVEL - 1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            lsum += lengths[y][i]
            y = parents[y][i]

    if x == y:
        return lsum

    for i in range(MAX_LEVEL - 1, -1, -1):
        if parents[x][i] == parents[y][i]:
            continue

        lsum += lengths[x][i]
        x = parents[x][i]

        lsum += lengths[y][i]
        y = parents[y][i]

    lsum += lengths[x][0] + lengths[y][0]
    return lsum


n = int(input())
MAX_LEVEL = int(math.log2(n)) + 1

lengths = [[0] * MAX_LEVEL for _ in range(n + 1)]
parents = [[0] * MAX_LEVEL for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)


for _ in range(n - 1):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

m = int(input())
answers = [list(map(int, input().split())) for _ in range(m)]


visited = [0] * (n + 1)
set_depth(1, 0)
connect()

for x, y in answers:
    print(LCA(x, y))
