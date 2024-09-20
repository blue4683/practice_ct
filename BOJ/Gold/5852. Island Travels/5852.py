from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


def get_island(sy, sx, number):
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        island[y][x] = number
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or grid[yy][xx] != 'X' or island[yy][xx]:
                continue

            q.append((yy, xx))


def numbering_island():
    number = 1
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'X' and not island[y][x]:
                get_island(y, x, number)
                number += 1

    return number - 1


def get_distance(sy, sx, number, graph):
    visited = [[INF] * c for _ in range(r)]
    heap = [(0, sy, sx)]
    while heap:
        distance, y, x = heappop(heap)
        if visited[y][x] <= distance:
            continue

        if island[y][x]:
            graph[number][island[y][x]] = min(
                graph[number][island[y][x]], distance)

        visited[y][x] = distance
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            next_distance = distance
            if out_of_range(yy, xx) or grid[yy][xx] == '.':
                continue

            if grid[yy][xx] == 'S':
                next_distance += 1

            heappush(heap, (next_distance, yy, xx))

    return graph


def set_graph():
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'X' and not visited[island[y][x]]:
                visited[island[y][x]] = 1
                graph = get_distance(y, x, island[y][x], graph)

    graph[0] = [0] * (n + 1)
    return graph


def get_swim(now, bit):
    if dp[now][bit]:
        return dp[now][bit]

    if bit == all_travel:
        dp[now][bit] = 0
        return dp[now][bit]

    result = INF
    for i in range(1, n + 1):
        if now == i or bit & (1 << i):
            continue

        result = min(result, get_swim(
            i, bit | (1 << i)) + graph[now][i])

    dp[now][bit] = result
    return dp[now][bit]


r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
island = [[0] * c for _ in range(r)]
n = numbering_island()

graph = set_graph()
dp = [[0] * (1 << (n + 1)) for _ in range(n + 1)]
all_travel = 0
for i in range(1, n + 1):
    all_travel |= 1 << i

print(get_swim(0, 0))
