from collections import deque
import sys
input = sys.stdin.readline
MAX = 100000


def bfs():
    q = deque([n])
    visited = [0] * MAX
    visited[n] = 1
    while q:
        x = q.popleft()
        if x == g:
            return visited[x] - 1

        if x + 1 < MAX and not visited[x + 1] and visited[x] <= t:
            visited[x + 1] = visited[x] + 1
            q.append(x + 1)

        if x and x * 2 < MAX and not visited[(x * 2) - (10 ** (len(str(x * 2)) - 1))] and visited[x] <= t:
            visited[(x * 2) - (10 ** (len(str(x * 2)) - 1))] = visited[x] + 1
            q.append((x * 2) - (10 ** (len(str(x * 2)) - 1)))

    return 'ANG'


n, t, g = map(int, input().split())
print(bfs())
