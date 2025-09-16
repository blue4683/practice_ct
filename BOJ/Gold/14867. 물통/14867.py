from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([(0, 0)])
    visited = defaultdict(int)
    visited[(0, 0)] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (c, d):
            return visited[(x, y)] - 1

        if not visited[(a, y)]:
            visited[(a, y)] = visited[(x, y)] + 1
            q.append((a, y))

        if not visited[(x, b)]:
            visited[(x, b)] = visited[(x, y)] + 1
            q.append((x, b))

        if not visited[(0, y)]:
            visited[(0, y)] = visited[(x, y)] + 1
            q.append((0, y))

        if not visited[(x, 0)]:
            visited[(x, 0)] = visited[(x, y)] + 1
            q.append((x, 0))

        if x != a and not visited[(a, y - (a - x)) if x + y > a else (x + y, 0)]:
            visited[(a, y - (a - x)) if x + y >
                    a else (x + y, 0)] = visited[(x, y)] + 1
            q.append((a, y - (a - x)) if x + y > a else (x + y, 0))

        if y != b and not visited[(x - (b - y), b) if x + y > b else (0, x + y)]:
            visited[(x - (b - y), b) if x + y >
                    b else (0, x + y)] = visited[(x, y)] + 1
            q.append((x - (b - y), b) if x + y > b else (0, x + y))

    return -1


a, b, c, d, = map(int, input().split())
print(bfs())
