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
arr = [''] + input().split()

edges = []
for _ in range(m):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()

graph = [i for i in range(n + 1)]
result = 0
cnt = 0
for d, u, v in edges:
    if arr[u] == arr[v] or find(u) == find(v):
        continue

    union(u, v)
    result += d
    cnt += 1

print(result) if cnt == n - 1 else print(-1)
