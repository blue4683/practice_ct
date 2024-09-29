from collections import defaultdict
import sys
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def out_of_range(y, x, y1, x1, y2, x2):
    if y < y1 or y > y2 or x < x1 or x > x2:
        return 1
    
    return 0


def check_two_colors(y1, x1, y2, x2):
    colors = set()
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            colors.add(grid[y][x])

    return 1 if len(colors) == 2 else 0


def bfs(y, x, y1, x1, y2, x2, visited):
    color = grid[y][x]
    q = [(y, x)]
    while q:
        y, x = q.pop()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx, y1, x1, y2, x2):
                continue

            if visited[yy][xx]:
                continue

            if grid[yy][xx] != color:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return visited


def check_contiguous(y1, x1, y2, x2):
    contiguous = defaultdict(int)
    visited = [[0] * n for _ in range(n)]
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            if visited[y][x]:
                continue
            
            contiguous[grid[y][x]] += 1
            visited = bfs(y, x, y1, x1, y2, x2, visited)

    cnts = sorted(contiguous.values())
    return 1 if cnts[0] == 1 and cnts[1] >= 2 else 0


def mark(y1, x1, y2, x2):
    for y3 in range(y1, y2 + 1):
        for x3 in range(x1, x2 + 1):
            for y4 in range(y3, y2 + 1):
                for x4 in range(x3, x2 + 1):
                    plcs[y3][x3][y4][x4] = 1


n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
plcs = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
result = 0
for ly in range(n - 1, -1, -1):
    for lx in range(n - 1, -1, -1):
        for y1 in range(n - ly):
            for x1 in range(n - lx):
                y2, x2 = y1 + ly, x1 + lx
                if plcs[y1][x1][y2][x2]:
                    continue

                if not check_two_colors(y1, x1, y2, x2):
                    continue
                
                cnt = check_contiguous(y1, x1, y2, x2)
                if cnt:
                    mark(y1, x1, y2, x2)
                    result += 1

print(result)
