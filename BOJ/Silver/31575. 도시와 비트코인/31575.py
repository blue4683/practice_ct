from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([(0, 0)])
    arr[0][0] = 0
    while q:
        y, x = q.popleft()
        if (y, x) == (m - 1, n - 1):
            return 'Yes'

        for dy, dx in [(0, 1), (1, 0)]:
            yy, xx = y + dy, x + dx
            if yy >= m or xx >= n or not arr[yy][xx]:
                continue

            arr[yy][xx] = 0
            q.append((yy, xx))

    return 'No'


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
print(bfs())
