import sys
input = sys.stdin.readline


def dfs(y, x):
    global result
    if x == 6:
        yy, xx = y + 1, 0

    else:
        yy, xx = y, x + 1

    if yy == 8 and xx == 0:
        result += 1
        return

    if not visited[yy][xx]:
        a = arr[yy][xx]
        if yy + 1 < 8 and not visited[yy + 1][xx] and (arr[yy][xx] + arr[yy + 1][xx]) not in used:
            b = arr[yy + 1][xx]
            if not used[a][b]:
                used[a][b] = 1
                used[b][a] = 1
                visited[yy][xx] = 1
                visited[yy + 1][xx] = 1
                dfs(yy, xx)
                visited[yy][xx] = 0
                visited[yy + 1][xx] = 0
                used[a][b] = 0
                used[b][a] = 0

        if xx + 1 < 7 and not visited[yy][xx + 1]:
            b = arr[yy][xx + 1]
            if not used[a][b]:
                used[a][b] = 1
                used[b][a] = 1
                visited[yy][xx] = 1
                visited[yy][xx + 1] = 1
                dfs(yy, xx)
                visited[yy][xx] = 0
                visited[yy][xx + 1] = 0
                used[a][b] = 0
                used[b][a] = 0

    else:
        dfs(yy, xx)


arr = [list(map(int, input().rstrip())) for _ in range(8)]

result = 0
visited = [[0] * 7 for _ in range(8)]
used = [[0] * 7 for _ in range(7)]
dfs(0, -1)

print(result)
