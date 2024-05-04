import sys
input = sys.stdin.readline


def get_dist(node, target, dist):
    global result
    for next, next_dist in graph[node]:
        if next == target:
            result = dist + next_dist
            return

        if not visited[next]:
            visited[next] = 1
            get_dist(next, target, dist + next_dist)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, d = map(int, input().split())
    graph[u].append([v, d])
    graph[v].append([u, d])

for _ in range(m):
    u, v = map(int, input().split())
    visited = [0] * (n + 1)
    visited[u] = 1
    result = 0
    get_dist(u, v, 0)
    print(result)
