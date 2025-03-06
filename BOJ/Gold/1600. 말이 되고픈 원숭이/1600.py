from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0), (2, 1), (2, -1),
     (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1

    return 0


def bfs():
    q = deque([(0, 0, 0)])
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    while q:
        y, x, cnt = q.popleft()
        if (y, x) == (h - 1, w - 1):
            return visited[h - 1][w - 1][cnt] - 1

        for i in range(12):
            if i > 3 and cnt == k:
                break

            dy, dx = d[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx]:
                continue

            if i > 3:
                if visited[yy][xx][cnt + 1]:
                    continue

                visited[yy][xx][cnt + 1] = visited[y][x][cnt] + 1
                q.append((yy, xx, cnt + 1))

            else:
                if visited[yy][xx][cnt]:
                    continue

                visited[yy][xx][cnt] = visited[y][x][cnt] + 1
                q.append((yy, xx, cnt))

    return -1


k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

result = bfs()
print(result)
