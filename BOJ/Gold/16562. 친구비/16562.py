import sys
input = sys.stdin.readline


def find(x):
    if x != graph[x]:
        graph[x] = find(graph[x])

    return graph[x]


def union(x, y):
    x, y = find(x), find(y)
    if arr[x - 1] > arr[y - 1]:
        graph[x] = y

    else:
        graph[y] = x


n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

edges = [(arr[i - 1], i, i) for i in range(1, n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    if v == w:
        continue

    edges.append((min(arr[v - 1], arr[w - 1]), v, w))

edges.sort()
graph = [i for i in range(n + 1)]
for cost, v, w in edges:
    if find(v) == find(w):
        continue

    union(v, w)

result = 0
visited = [0] * (n + 1)
for i in range(1, n + 1):
    find(i)
    if visited[graph[i]]:
        continue

    visited[graph[i]] = 1
    result += arr[graph[i] - 1]

print(result) if result <= k else print('Oh no')
