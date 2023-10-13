from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def BFS():
    q = deque([(0, 0, 1)])
    visited[0][0] = [1, 1]

    while q:
        y, x, c= q.popleft()
        for dy, dx in d:
            yy, xx, cc = y + dy, x + dx, c

            if 0 > yy or yy > n - 1 or 0 > xx or xx > m - 1: continue
            if not cc and arr[yy][xx]: continue
            if visited[yy][xx][cc] == 21e8:
                if arr[yy][xx]:
                    if cc:
                        cc = 0
                        visited[yy][xx][cc] = visited[y][x][cc + 1] + 1

                else:
                    visited[yy][xx][cc] = visited[y][x][cc] + 1

                q.append((yy, xx, cc))

n, m = map(int,input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[[21e8, 21e8] for _ in range(m)] for _ in range(n)]

BFS()

print(-1) if visited[n - 1][m - 1] == [21e8, 21e8] else print(min(visited[n - 1][m - 1]))