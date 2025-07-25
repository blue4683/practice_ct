from collections import deque
import sys
input = sys.stdin.readline
MOD = 1000007


def out_of_range(y, x):
    if y >= n or x >= m:
        return 1

    return 0


def bfs():
    visited = [[[[0] * (c + 2) for _ in range(c + 1)]
                for _ in range(m)] for _ in range(n)]
    if arr[0][0]:
        q = deque([(0, 0, 1, arr[0][0])])
        visited[0][0][1][arr[0][0]] = 1
        dp[0][0][1][arr[0][0]] = 1

    else:
        q = deque([(0, 0, 0, 0)])
        visited[0][0][0][0] = 1
        dp[0][0][0][0] = 1

    while q:
        y, x, cnt, before = q.popleft()
        if (y, x) == (n - 1, m - 1):
            continue

        for dy, dx in [(0, 1), (1, 0)]:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            if not arr[yy][xx]:
                dp[yy][xx][cnt][before] += dp[y][x][cnt][before]
                dp[yy][xx][cnt][before] %= MOD
                if not visited[yy][xx][cnt][before]:
                    visited[yy][xx][cnt][before] = 1
                    q.append((yy, xx, cnt, before))

            elif before < arr[yy][xx] and cnt < c:
                dp[yy][xx][cnt + 1][arr[yy][xx]] += dp[y][x][cnt][before]
                dp[yy][xx][cnt + 1][arr[yy][xx]] %= MOD
                if not visited[yy][xx][cnt + 1][arr[yy][xx]]:
                    visited[yy][xx][cnt + 1][arr[yy][xx]] = 1
                    q.append((yy, xx, cnt + 1, arr[yy][xx]))


n, m, c = map(int, input().split())
arr = [[0] * m for _ in range(n)]
index = 1
for y, x in [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(c)]:
    arr[y][x] = index
    index += 1

dp = [[[[0] * (c + 2) for _ in range(c + 1)]
       for _ in range(m)] for _ in range(n)]
bfs()
for i in range(c + 1):
    print(sum(dp[n - 1][m - 1][i]) % MOD, end=' ')
