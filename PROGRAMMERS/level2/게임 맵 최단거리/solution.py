from collections import deque

def bfs(maps, visited, d, n, m):
    q = deque([(0,0)])
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for dy,dx in d:
            yy,xx = y+dy, x+dx
            if 0<=yy<n and 0<=xx<m and maps[yy][xx]==1 and visited[y][x]+1<visited[yy][xx]:
                visited[yy][xx] = visited[y][x]+1
                if yy==n-1 and xx==m-1:
                    return visited[yy][xx]
                q+=[(yy,xx)]
    return -1

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    visited=[[1e9]*m for _ in range(n)]
    answer = bfs(maps, visited, d, n, m)
    return answer