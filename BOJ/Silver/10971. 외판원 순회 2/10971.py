import sys
input = sys.stdin.readline


def dfs(x, c):
    global result
    if c > result:
        return

    if 0 not in visited:
        if arr[x][0]:
            result = min(result, c + arr[x][0])

        return

    for xx in range(n):
        if visited[xx] or not arr[x][xx]:
            continue

        visited[xx] = 1
        dfs(xx, c + arr[x][xx])
        visited[xx] = 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = float('inf')
visited = [0] * n
visited[0] = 1
dfs(0, 0)

print(result)
