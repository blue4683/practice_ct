def out_of_range(y, x):
    return y < 0 or y >= n or x < 0 or x >= m


def bfs(sy, sx):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = [(sy, sx)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or not arr[yy][xx]:
                continue
            
            visited[yy][xx] = 1
            q.append((yy, xx))
            

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
result = 0
for y in range(n):
    for x in range(m):
        if not arr[y][x] or visited[y][x]:
            continue
        
        visited[y][x] = 1
        bfs(y, x)
        result += 1
        
print(result)
