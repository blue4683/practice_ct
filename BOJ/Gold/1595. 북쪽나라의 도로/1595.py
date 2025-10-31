import sys
input = sys.stdin.readline


def dfs(now, dist):
    global x, result
    leaf = 1
    for node, d in graph[now]:
        if visited[node]:
            continue

        visited[node] = 1
        dfs(node, dist + d)
        leaf = 0

    if leaf:
        if result < dist:
            x, result = now, dist


x, result = 0, 0
graph = [[] for _ in range(10001)]
while 1:
    try:
        a, b, c = map(int, input().split())
        x = a
        graph[a].append((b, c))
        graph[b].append((a, c))

    except:
        break

visited = [0] * 10001
visited[x] = 1
dfs(x, 0)

visited = [0] * 10001
visited[x] = 1
dfs(x, 0)

print(result)
