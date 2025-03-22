from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([(a, b, c)])
    while q:
        x, y, z = q.popleft()
        if set([x, y, z]) == {x}:
            return 1

        for i, j, k in [(x, y, z), (x, z, y), (y, z, x)]:
            if i == j:
                continue

            i, j = sorted([i, j])
            xx, yy, zz = i + i, j - i, k
            if visited[(xx, yy, zz)]:
                continue

            visited[(xx, yy, zz)] = 1
            q.append((xx, yy, zz))

    return 0


a, b, c = map(int, input().split())
visited = defaultdict(int)
print(bfs())
