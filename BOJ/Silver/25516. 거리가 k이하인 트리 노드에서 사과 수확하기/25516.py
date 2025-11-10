from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    result = arr[0]
    q = deque([0])
    visited = [-1] * n
    visited[0] = 0
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if visited[xx] != -1:
                continue

            result += arr[xx]
            visited[xx] = visited[x] + 1
            if visited[xx] >= k:
                continue

            q.append(xx)

    return result


n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arr = list(map(int, input().split()))
print(bfs())
