def dfs(depth, st):
    global result
    if depth == n//2:
        start = 0
        link = 0
        for y in range(n):
            for x in range(n):
                if not visited[y] and not visited[x]:
                    link += stats[y][x]
                if visited[y] and visited[x]:
                    start += stats[y][x]
        result = min(result, abs(start - link))

    for i in range(st, n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i)
            visited[i] = 0

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
result = 1e9
dfs(0, 0)
print(result)