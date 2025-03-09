from collections import deque
import sys
input = sys.stdin.readline
d = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


def out_of_range(y, x):
    if y < 0 or y >= l or x < 0 or x >= l:
        return 1

    return 0


def bfs(sy, sx):
    visited = [[0] * l for _ in range(l)]
    visited[sy][sx] = 1
    q = deque([(sy, sx, 0)])
    while q:
        y, x, cnt = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if (yy, xx) == end:
                return cnt + 1

            visited[yy][xx] = 1
            q.append((yy, xx, cnt + 1))

    return -1


for _ in range(int(input())):
    l = int(input())
    y, x = map(int, input().split())
    end = tuple(map(int, input().split()))
    if (y, x) == end:
        print(0)

    else:
        print(bfs(y, x))
