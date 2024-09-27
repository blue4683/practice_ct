from collections import deque
import sys
input = sys.stdin.readline


def bfs(s, sign, copied_visited):
    cnt = 0
    q = deque([(s, sign)])
    while q:
        now, now_sign = q.popleft()
        if copied_visited[now] == now_sign:
            continue

        if visited[now] and visited[now] != now_sign:
            return -1, copied_visited

        copied_visited[now] = now_sign
        if now_sign == 1:
            cnt += 1

        for node in graph[now]:
            if not copied_visited[node]:
                q.append((node, -now_sign))
                continue

            if copied_visited[node] != -now_sign:
                return -1, copied_visited

    return cnt, copied_visited


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
result = -1
for i in range(1, n + 1):
    if visited[i]:
        continue

    cnt1, visited1 = bfs(i, 1, visited[:])
    cnt2, visited2 = bfs(i, -1, visited[:])

    if (cnt1, cnt2) == (-1, -1):
        break

    elif cnt1 >= cnt2:
        visited = visited1

    else:
        visited = visited2

else:
    result = visited.count(1)

print(result)
