import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
graph = [[set(), set()] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][0].add(b)
    graph[b][1].add(a)

result = 0
for i in range(1, n + 1):
    q = list(graph[i][0])
    while q:
        now = q.pop()
        for node in graph[now][0]:
            if node in graph[i][0]:
                continue

            graph[i][0].add(node)
            q.append(node)

    q = list(graph[i][1])
    while q:
        now = q.pop()
        for node in graph[now][1]:
            if node in graph[i][1]:
                continue

            graph[i][1].add(node)
            q.append(node)

    if len(graph[i][0]) > n // 2 or len(graph[i][1]) > n // 2:
        result += 1

print(result)
