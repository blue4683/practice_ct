from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_possible(diff):
    sy, sx = waypoints[0]
    visited = [[0] * n for _ in range(m)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < m and 0 <= xx < n and not visited[yy][xx]:
                height = abs(course[yy][xx] - course[y][x])
                if height > diff:
                    continue

                visited[yy][xx] = 1
                q.append((yy, xx))

    for y, x in waypoints:
        if not visited[y][x]:
            return 0

    return 1


m, n = map(int, input().split())
course = [list(map(int, input().split())) for _ in range(m)]
arr = [list(map(int, input().split())) for _ in range(m)]
waypoints = [(y, x) for y in range(m) for x in range(n) if arr[y][x]]
result = 0
l, r = 0, max(map(max, course))
while l <= r:
    mid = (l + r) // 2
    if is_possible(mid):
        result = mid
        r = mid - 1

    else:
        l = mid + 1

print(result)
