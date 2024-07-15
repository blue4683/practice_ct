from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_dist():
    result = 200
    for i in range(len(pos)):
        y, x, index = pos[i]
        for j in range(i + 1, len(pos)):
            yy, xx, iindex = pos[j]
            if index == iindex:
                continue

            result = min(result, abs(y - yy) + abs(x - xx) - 1)
            if result == 1:
                return result

    return result


def get_pos(sy, sx, index):
    visited[sy][sx] = 1
    q = deque([(sy, sx, index)])

    while q:
        y, x, i = q.popleft()
        pos.append((y, x, i))
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n and arr[yy][xx] and not visited[yy][xx]:
                visited[yy][xx] = 1
                q.append((yy, xx, i))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = []

index = 1
visited = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if arr[y][x] and not visited[y][x]:
            get_pos(y, x, index)
            index += 1


print(get_dist())
