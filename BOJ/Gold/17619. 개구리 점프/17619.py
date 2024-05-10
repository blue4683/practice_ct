import sys
input = sys.stdin.readline


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if x > y:
        graph[x] = y

    else:
        graph[y] = x


def check(x1, x2, x11, x22):
    if x11 <= x1 <= x22 or x11 <= x2 <= x22 or x1 <= x11 <= x2 or x1 <= x22 <= x2:
        return 1

    return 0


n, q = map(int, input().split())
logs = []
for i in range(1, n + 1):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, y, i))

logs.sort()
graph = [i for i in range(n + 1)]

start, end, _, num = logs[0]
for i in range(1, n):
    x1, x2, y, i = logs[i]
    if check(start, end, x1, x2):
        union(i, num)
        start = min(start, x1)
        end = max(end, x2)

    else:
        start, end, num = x1, x2, i

for _ in range(q):
    a, b = map(int, input().split())
    print(1) if find(a) == find(b) else print(0)
