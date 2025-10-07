from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def out_of_range(x, y):
    if y < 0 or y > t or x < 0 or x > 10 ** 6:
        return 1

    return 0


def bfs():
    q = deque([(0, 0)])
    visited = defaultdict(int)
    visited[(0, 0)] = 1
    while q:
        x, y = q.popleft()
        if y == t:
            return visited[(x, y)] - 1

        for dx in range(-2, 3):
            for dy in range(-2, 3):
                xx, yy = x + dx, y + dy
                if out_of_range(xx, yy) or visited[(xx, yy)] or not hole[(xx, yy)]:
                    continue

                visited[(xx, yy)] = visited[(x, y)] + 1
                q.append((xx, yy))

    return -1


n, t = map(int, input().split())
hole = defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    hole[(x, y)] = 1

print(bfs())
