from collections import deque
import sys
input = sys.stdin.readline


def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()

        for next, cost in graph[now]:
            if sum(result[now]) == 0:
                result[next][now] += cost

            else:
                for i in range(1, n + 1):
                    result[next][i] += result[now][i] * cost

            indegree[next] -= 1
            if not indegree[next]:
                q.append(next)


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    x, y, k = map(int, input().split())
    indegree[x] += 1
    graph[y].append((x, k))

result = [[0] * (n + 1) for _ in range(n + 1)]
topology_sort()

for enum in enumerate(result[n]):
    if enum[1] > 0:
        print(*enum)
