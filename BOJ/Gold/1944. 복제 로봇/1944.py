from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(sy, sx, i):
    edge = []
    q = deque([(sy, sx)])
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or arr[yy][xx] == '1':
                continue

            visited[yy][xx] = visited[y][x] + 1
            if arr[yy][xx] != '0':
                j = pos.index((yy, xx))
                edge.append((visited[yy][xx] - 1, i, j))

            q.append((yy, xx))

    return edge


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return 0

    elif x > y:
        graph[x] = y
        return 1

    else:
        graph[y] = x
        return 1


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

edges = []
pos = [(y, x) for y in range(n) for x in range(n) if not arr[y][x].isnumeric()]
for i in range(m + 1):
    y, x = pos[i]
    edges.extend(bfs(y, x, i))

edges.sort()
graph = [i for i in range(m + 1)]
result = 0
for cost, a, b in edges:
    if union(a, b):
        result += cost
        m -= 1

print(result) if not m else print(-1)
