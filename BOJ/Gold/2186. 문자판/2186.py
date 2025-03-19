import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def dfs(y, x, depth):
    if dp[y][x][depth] != -1:
        return dp[y][x][depth]

    if depth == l - 1:
        return 1

    cnt = 0
    for dk in range(1, k + 1):
        for dy, dx in d:
            yy, xx = y + dy * dk, x + dx * dk
            if out_of_range(yy, xx) or arr[yy][xx] != word[depth + 1]:
                continue

            cnt += dfs(yy, xx, depth + 1)

    dp[y][x][depth] = cnt
    return dp[y][x][depth]


n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
word = input().rstrip()
l = len(word)

result = 0
dp = [[[-1] * l for _ in range(m)] for _ in range(n)]
for y in range(n):
    for x in range(m):
        if arr[y][x] == word[0]:
            result += dfs(y, x, 0)

print(result)
