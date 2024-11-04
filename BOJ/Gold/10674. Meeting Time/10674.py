from collections import deque
import sys
input = sys.stdin.readline


def get_times(visited, index):
    visited[0][0] = 1
    q = deque([(0, 1)])
    while q:
        time, now = q.popleft()
        for field in graph[now]:
            next_time = time + field[index]
            if visited[field[0]][next_time]:
                continue

            visited[field[0]][next_time] = 1
            q.append((next_time, field[0]))

    return visited


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c, d = map(int, input().split())
    graph[a].append((b, c, d))

dp_b = get_times([[0] * (100 * n) for _ in range(n + 1)], 1)
dp_e = get_times([[0] * (100 * n) for _ in range(n + 1)], 2)

result = 'IMPOSSIBLE'
for i in range(100 * n):
    if dp_b[n][i] and dp_e[n][i]:
        result = i
        break

print(result)
