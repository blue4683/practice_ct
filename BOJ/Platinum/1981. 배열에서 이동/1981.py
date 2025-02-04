from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def bfs(a, b):
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0)])

    while q:
        y, x = q.popleft()
        if (y, x) == (n - 1, n - 1):
            return 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if not a <= arr[yy][xx] <= b:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx))

    return 0


def check(mid):
    for i in range(minv, maxv + 1):
        if not (i <= s <= i + mid and i <= e <= i + mid):
            continue

        if bfs(i, i + mid):
            return 1

    return 0


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
s, e = arr[0][0], arr[n - 1][n - 1]

minv, maxv = 201, -1
for y in range(n):
    for x in range(n):
        minv = min(minv, arr[y][x])
        maxv = max(maxv, arr[y][x])

result = 0
left, right = 0, maxv
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        result = mid
        right = mid - 1

    else:
        left = mid + 1

print(result)
