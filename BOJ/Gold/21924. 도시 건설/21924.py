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
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[-1])

cnt = 0
total = 0
cost = 0
graph = [i for i in range(n + 1)]
for a, b, c in edges:
    total += c
    if find(a) == find(b):
        continue

    union(a, b)
    cnt += 1
    cost += c

print(total - cost) if cnt == n - 1 else print(-1)
