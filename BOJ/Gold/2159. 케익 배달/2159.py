import sys
input = sys.stdin.readline
d = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]
INF = float('inf')


def out_of_range(y, x):
    if y < 0 or y > 100000 or x < 0 or x > 100000:
        return 1

    return 0


def get_distance(y, x, yy, xx):
    return abs(y - yy) + abs(x - xx)


n = int(input())
sy, sx = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF] * 5 for _ in range(n)]
for i in range(n):
    y, x = pos[i]
    for j in range(5):
        dy, dx = d[j]
        yy, xx = y + dy, x + dx
        if out_of_range(yy, xx):
            continue

        if not i:
            dp[i][j] = min(dp[i][j], get_distance(sy, sx, yy, xx))
            continue

        for k in range(5):
            ddy, ddx = d[k]
            yyy, xxx = pos[i - 1][0] + ddy, pos[i - 1][1] + ddx
            if out_of_range(yyy, xxx):
                continue

            dp[i][j] = min(dp[i][j], dp[i - 1][k] +
                           get_distance(yy, xx, yyy, xxx))

print(min(dp[n - 1]))
