from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    result = 0
    cnt = 0
    q = deque([n])
    visited = [10 ** 9] * 100001
    visited[n] = 1
    while q:
        x = q.popleft()
        if x == k:
            result = visited[x] - 1
            cnt += 1
            continue

        if x - 1 >= 0 and visited[x - 1] >= visited[x] + 1:
            visited[x - 1] = visited[x] + 1
            q.append(x - 1)

        if x + 1 < 100001 and visited[x + 1] >= visited[x] + 1:
            visited[x + 1] = visited[x] + 1
            q.append(x + 1)

        if x * 2 < 100001 and visited[x * 2] >= visited[x] + 1:
            visited[x * 2] = visited[x] + 1
            q.append(x * 2)

    return result, cnt


n, k = map(int, input().split())
result = bfs()
for res in result:
    print(res)
