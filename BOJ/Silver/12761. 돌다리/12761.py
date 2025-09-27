from collections import deque
import sys
input = sys.stdin.readline


def out_of_range(x):
    if x < 0 or x > 100000:
        return 1

    return 0


def bfs():
    q = deque([n])
    visited = [0] * 100001
    visited[n] = 1
    while q:
        x = q.popleft()
        if x == m:
            return visited[m] - 1

        for dx in d:
            xx = x + dx
            if out_of_range(xx) or visited[xx]:
                continue

            visited[xx] = visited[x] + 1
            q.append(xx)

        for dx in [a, b]:
            xx = x * dx
            if out_of_range(xx) or visited[xx]:
                continue

            visited[xx] = visited[x] + 1
            q.append(xx)

    return visited[m] - 1


a, b, n, m = map(int, input().split())
d = [1, -1, a, b, -a, -b]
print(bfs())
