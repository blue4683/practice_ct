from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


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

    else:
        graph[y] = x

    return 1


def bfs(q, cnt):
    year = 0
    while cnt != 1:
        new_q = []
        while q:
            y, x = q.popleft()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx):
                    continue

                if arr[yy][xx] and union(arr[yy][xx], arr[y][x]):
                    cnt -= 1
                    continue

                if visited[yy][xx]:
                    continue

                visited[yy][xx] = 1
                arr[yy][xx] = arr[y][x]
                new_q.append((yy, xx))

        for y, x in new_q:
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or not arr[yy][xx]:
                    continue

                if union(arr[yy][xx], arr[y][x]):
                    cnt -= 1

        q = deque(new_q)
        year += 1

    return year


n, k = map(int, input().split())
arr = [[0] * n for _ in range(n)]
graph = [i for i in range(k + 1)]
visited = [[0] * n for _ in range(n)]
q = deque()
cnt = k
for i in range(1, k + 1):
    y, x = map(lambda x: int(x) - 1, input().split())
    visited[y][x] = 1
    q.append((y, x))
    arr[y][x] = i
    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx) or not arr[yy][xx]:
            continue

        if union(arr[y][x], arr[yy][xx]):
            cnt -= 1

print(bfs(q, cnt))
