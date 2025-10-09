from collections import deque
import sys
input = sys.stdin.readline


def get_dist(y1, x1, y2, x2):
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


def bfs(fuel):
    q = deque([(0, 0, 0, fuel)])
    visited = [0] * (n + 1)
    while q:
        y, x, cnt, f = q.popleft()
        if (y, x) == (10000, 10000):
            return 1

        for i in range(n + 1):
            if visited[i]:
                continue

            yy, xx = pos[i]
            dist = get_dist(y, x, yy, xx) / 10
            if dist > f:
                if cnt == k or fuel < dist:
                    continue

                visited[i] = 1
                q.append((yy, xx, cnt + 1, fuel))

            else:
                visited[i] = 1
                q.append((yy, xx, cnt, f - dist))

    return 0


n, k = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(n)]

pos.sort(key=lambda x: get_dist(0, 0, *x))
pos.append((10000, 10000))
l, r = 0, 15000
while l <= r:
    mid = (l + r) // 2
    if bfs(mid):
        r = mid - 1

    else:
        l = mid + 1

print(l)
