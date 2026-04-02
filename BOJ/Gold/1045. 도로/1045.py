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


n, m = map(int, input().split())
edges = []
for i in range(n):
    arr = list(map(lambda x: int(x == 'Y'), list(input().rstrip())))
    for j in range(i + 1, n):
        if arr[j]:
            edges.append((i, j))

graph = [i for i in range(n)]
used = set()
for x, y in edges:
    if find(x) != find(y):
        union(x, y)
        used.add((x, y))

if len(used) != n - 1:
    print(-1)
    exit()

for road in edges:
    if road not in used:
        used.add(road)

    if len(used) == m:
        break

if len(used) != m:
    print(-1)

else:
    result = [0] * n
    for x, y in used:
        result[x] += 1
        result[y] += 1

    print(*result)
