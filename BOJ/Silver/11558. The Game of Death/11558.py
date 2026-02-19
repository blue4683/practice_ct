import sys
input = sys.stdin.readline


def bfs():
    visited = [-1] * (n + 1)
    visited[1] = 0
    q = [1]
    while q:
        x = q.pop()
        xx = graph[x]
        if visited[xx] != -1:
            continue

        visited[xx] = visited[x] + 1
        q.append(xx)

    return visited[n] if visited[n] != -1 else 0


for _ in range(int(input())):
    n = int(input())
    graph = [0] + [int(input()) for _ in range(n)]
    print(bfs())
