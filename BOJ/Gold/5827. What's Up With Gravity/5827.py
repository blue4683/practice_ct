from heapq import *
import sys
input = sys.stdin.readline
INF = 10 ** 9

d = [(0, -1), (0, 1)]
up_down = [(-1, 0), (1, 0)]

def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1
    
    return 0


def fall(y, x, dir):
    dy, dx = up_down[dir]
    while grid[y][x] in ['.', 'C']:
        y += dy
        x += dx
        if out_of_range(y, x):
            return -1, 0
        
        if grid[y][x] == 'D':
            return 0, -1

    return y - dy, x - dx


def traverse(sy, sx):
    visited = [[0] * m for _ in range(n)]
    sy, sx = fall(sy, sx, 1)
    if (sy, sx) == (-1, 0):
        return -1
    
    heap = [(0, 1, sy, sx)]
    while heap:
        cnt, is_down, y, x = heappop(heap)
        for i in range(2):
            if visited[y][x] & (1 << i):
                continue

            dy, dx = d[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or grid[yy][xx] == '#':
                continue

            if grid[yy][xx] == 'D':
                return cnt

            yy, xx = fall(yy, xx, is_down)
            if (yy, xx) == (-1, 0):
                continue

            if (yy, xx) == (0, -1):
                return cnt

            visited[y][x] |= (1 << i)
            heappush(heap, (cnt, is_down, yy, xx))

        is_down ^= 1
        if visited[y][x] & (1 << (is_down + 2)):
            continue

        cnt += 1
        yy, xx = fall(y, x, is_down)
        if (yy, xx) == (-1, 0):
            continue

        if (yy, xx) == (0, -1):
            return cnt

        visited[y][x] |= (1 << (is_down + 2))
        heappush(heap, (cnt, is_down, yy, xx))

    return -1


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
sy, sx = [(y, x) for y in range(n) for x in range(m) if grid[y][x] == 'C'][0]
print(traverse(sy, sx))
