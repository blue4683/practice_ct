from collections import deque
import sys
input = sys.stdin.readline


def bfs(i):
    q = deque([i])
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx] == -1:
                visited[xx] = visited[x] ^ 1
                q.append(xx)

            elif visited[xx] == visited[x]:
                return 0

    return 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    possible = 1
    visited = [-1] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] != -1:
            continue

        visited[i] = 0
        if not bfs(i):
            possible = 0
            break

    print('impossible') if not possible else print('possible')
