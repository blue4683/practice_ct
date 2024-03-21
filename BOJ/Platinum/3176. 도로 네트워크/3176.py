import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def set_depth(parent, now, dep, distance):
    depth[now] = dep
    parents[now][0] = parent
    short_distance[now][0] = distance
    long_distance[now][0] = distance

    for next, dist in graph[now]:
        if next != parent:
            set_depth(now, next, dep + 1, dist)


def connect():
    for i in range(1, MAX_LEVEL):
        for cur in range(2, n + 1):
            parent = parents[cur][i - 1]
            if parent == 0:
                continue

            parents[cur][i] = parents[parent][i - 1]
            short_distance[cur][i] = min(
                short_distance[parent][i - 1], short_distance[cur][i - 1])
            long_distance[cur][i] = max(
                long_distance[parent][i - 1], long_distance[cur][i - 1])


def LCA(x, y):
    if depth[x] > depth[y]:
        x, y = y, x

    short_dist, long_dist = 10 ** 6, 0

    for i in range(MAX_LEVEL - 1, -1, -1):
        if depth[y] - depth[x] >= 1 << i:
            short_dist = min(short_dist, short_distance[y][i])
            long_dist = max(long_dist, long_distance[y][i])
            y = parents[y][i]

    if x == y:
        return short_dist, long_dist

    for i in range(MAX_LEVEL - 1, -1, -1):
        if parents[x][i] == parents[y][i]:
            continue

        short_dist = min(
            short_dist, short_distance[x][i], short_distance[y][i])
        long_dist = max(long_dist, long_distance[x][i], long_distance[y][i])

        x = parents[x][i]
        y = parents[y][i]

    short_dist = min(short_dist, short_distance[x][0], short_distance[y][0])
    long_dist = max(long_dist, long_distance[x][0], long_distance[y][0])

    return short_dist, long_dist


n = int(input())
MAX_LEVEL = int(math.log2(n)) + 1

short_distance = [[10 ** 6] * MAX_LEVEL for _ in range(n + 1)]
long_distance = [[0] * MAX_LEVEL for _ in range(n + 1)]
parents = [[0] * MAX_LEVEL for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

k = int(input())
answers = [list(map(int, input().split())) for _ in range(k)]

set_depth(0, 1, 0, 0)
connect()

for x, y in answers:
    print(*LCA(x, y))
