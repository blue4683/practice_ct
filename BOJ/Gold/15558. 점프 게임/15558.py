from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [[0] * n for _ in range(2)]
    visited[0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        y, x, t = q.popleft()
        for dy, dx in d:
            yy, xx = y ^ dy, x + dx
            if xx >= n:
                return 1

            if xx <= t or not arr[yy][xx] or visited[yy][xx]:
                continue

            visited[yy][xx] = 1
            q.append((yy, xx, t + 1))

    return 0


n, k = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(2)]
d = [(0, 1), (0, -1), (1, k)]
print(bfs())
