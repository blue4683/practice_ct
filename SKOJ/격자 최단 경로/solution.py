from collections import deque

def out_of_range(y, x):
    return y < 0 or y >= n or x < 0 or x >= m


def bfs():
    q = deque([(0, 0)])
    visited =[[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if (y, x) == (n - 1, m - 1):
            return visited[y][x] - 1
        
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or not arr[yy][xx]:
                continue
            
            visited[yy][xx] = visited[y][x] + 1
            q.append((yy, xx))
            
    return -1


d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

print(bfs())
