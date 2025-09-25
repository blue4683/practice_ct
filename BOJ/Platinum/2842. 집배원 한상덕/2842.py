from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(l, r):
    if dist[sy][sx] < l or dist[sy][sx] > r:
        return 0

    cnt = 0
    visited = [[0] * n for _ in range(n)]
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        if cnt == len(dest):
            return 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx] or dist[yy][xx] < l or dist[yy][xx] > r:
                continue

            visited[yy][xx] = 1
            if (yy, xx) in dest:
                cnt += 1

            q.append((yy, xx))

    return 0


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
dist = [list(map(int, input().split())) for _ in range(n)]

sy, sx = [(y, x) for y in range(n) for x in range(n) if arr[y][x] == 'P'][0]
dest = set([(y, x) for y in range(n) for x in range(n) if arr[y][x] == 'K'])
heights = sorted(set([dist[y][x] for y in range(n) for x in range(n)]))
l, r = 0, 0
result = 10 ** 9
while r < len(heights) and l <= r:
    while l <= r and bfs(heights[l], heights[r]):
        result = min(result, heights[r] - heights[l])
        l += 1

    r += 1

print(result)
