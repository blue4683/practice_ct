from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9

d = [-1, 0, 1]


def bfs():
    q = deque([(space[0][i], 0, i, 2) for i in range(m)])
    while q:
        cost, y, x, dir = q.popleft()
        for dx in d:
            if dx == dir:
                continue

            yy = y + 1
            xx = x + dx
            if 0 <= xx < m:
                new_cost = cost + space[yy][xx]
                if yy == n - 1:
                    dp[xx] = min(dp[xx], new_cost)
                    continue

                q.append((new_cost, yy, xx, dx))

    return min(dp)


n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
dp = [INF] * m
print(bfs())
