from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([0])
    visited = [0] * n
    visited[0] = 1
    while q:
        x = q.popleft()
        if x == k:
            return visited[x] - 1

        xx = graph[x]
        if visited[xx]:
            continue

        visited[xx] = visited[x] + 1
        q.append(xx)

    return -1


n, k = map(int, input().split())
graph = [int(input()) for _ in range(n)]
print(bfs())
