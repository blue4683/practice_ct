from collections import deque


def bfs(sy, sx, dest, maps, n, m):
    INF = 10 ** 9
    q = deque([(sy, sx)])
    visited = [[INF] * m for _ in range(n)]
    visited[sy][sx] = 0
    d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    while q:
        y, x = q.popleft()
        if maps[y][x] == dest:
            return visited[y][x]
        
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if yy < 0 or yy >= n or xx < 0 or xx >= m or maps[yy][xx] == 'X':
                continue
                
            if visited[yy][xx] <= visited[y][x] + 1:
                continue
            
            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))
            
    return -1


def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    sy, sx = [(y, x) for y in range(n) for x in range(m) if maps[y][x] == 'S'][0]
    ly, lx = [(y, x) for y in range(n) for x in range(m) if maps[y][x] == 'L'][0]
    a, b = bfs(sy, sx, 'L', maps, n, m), bfs(ly, lx, 'E', maps, n, m)
    if -1 not in (a, b):
        answer = a + b
        
    return answer
