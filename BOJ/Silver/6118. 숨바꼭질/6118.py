import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


result = [0, 0, 0]
q = [1]
visited = [0] * (n + 1)
visited[1] = 1
while q:
    now = q.pop()
    for node in graph[now]:
        if not visited[node] or visited[node] > visited[now] + 1:
            visited[node] = visited[now] + 1
            q.append(node)

for i in range(1, n + 1):
    if result[1] > visited[i] - 1:
        continue

    elif result[1] < visited[i] - 1:
        result = [i, visited[i] - 1, 1]

    else:
        result[-1] += 1

print(*result)
