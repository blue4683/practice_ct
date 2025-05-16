from collections import defaultdict, deque
import sys
input = sys.stdin.readline
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]


def out_of_range(y, x):
    if y < 0 or y > n or x < 0 or x > n:
        return 1

    return 0


def bfs():
    visited = defaultdict(int)
    visited[(y1, x1)] = 1
    q = deque([(y1, x1)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[(yy, xx)]:
                continue

            if (yy, xx) == (y2, x2):
                return visited[(y, x)]

            visited[(yy, xx)] = visited[(y, x)] + 1
            q.append((yy, xx))

    return -1


n = int(input())
y1, x1, y2, x2 = map(int, input().split())
print(bfs())
