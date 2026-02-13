import sys
input = sys.stdin.readline
INF = 10 ** 9


n, m = map(int, input().split())
graph = [set() for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

result = INF
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if j not in graph[i]:
            continue

        for k in range(j + 1, n + 1):
            if k not in graph[i] or k not in graph[j]:
                continue

            result = min(result, len(graph[i]) +
                         len(graph[j]) + len(graph[k]) - 6)

print(result) if result != INF else print(-1)
