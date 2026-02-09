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


n, m, k = map(int, input().split())
edges = [(i, *map(int, input().split())) for i in range(1, m + 1)]
edges.sort(reverse=True)

result = []
for _ in range(k):
    connected = 0
    graph = [i for i in range(n + 1)]
    score = 0
    for i in range(len(edges) - 1, -1, -1):
        if connected == n - 1:
            break

        w, x, y = edges[i]
        if find(x) == find(y):
            continue

        union(x, y)
        score += w
        connected += 1

    score = 0 if connected != n - 1 else score
    result.append(score)
    edges.pop()

print(*result)
