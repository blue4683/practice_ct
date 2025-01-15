import sys
input = sys.stdin.readline
INF = 10 ** 9
d = [(0, -1), (-1, -1), (-1, 0), (-1, 1)]
k = 1


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= 3:
        return 1

    return 0


while 1:
    n = int(input())
    if not n:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][1] = graph[0][1]
    for y in range(n):
        for x in range(3):
            if (y, x) == (0, 1):
                continue

            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx):
                    continue

                dp[y][x] = min(dp[y][x], dp[yy][xx] + graph[y][x])

    print(f'{k}. {dp[n - 1][1]}')
    k += 1
