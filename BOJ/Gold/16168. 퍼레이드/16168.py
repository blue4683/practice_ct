import sys
input = sys.stdin.readline


def bfs():
    q = [1]
    visited = [0] * (v + 1)
    visited[1] = 1
    while q:
        x = q.pop()
        for xx in graph[x]:
            if visited[xx]:
                continue

            visited[xx] = 1
            q.append(xx)

    for i in range(1, v + 1):
        if not visited[i]:
            return 0

    return 1


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

odd = 0
for i in range(1, v + 1):
    if len(graph[i]) % 2:
        odd += 1

if odd in {0, 2} and bfs():
    print('YES')

else:
    print('NO')
