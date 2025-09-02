from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    coins = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'o']
    q = deque([(*coins[0], *coins[1])])
    for t in range(1, 11):
        new_q = []
        while q:
            y1, x1, y2, x2 = q.popleft()
            for dy, dx in d:
                yy1, xx1 = y1 + dy, x1 + dx
                yy2, xx2 = y2 + dy, x2 + dx
                out1, out2 = out_of_range(yy1, xx1), out_of_range(yy2, xx2)
                if out1 ^ out2:
                    return t

                if out1 and out2:
                    continue

                if arr[yy1][xx1] == '#':
                    yy1, xx1 = y1, x1

                if arr[yy2][xx2] == '#':
                    yy2, xx2 = y2, x2

                new_q.append((yy1, xx1, yy2, xx2))

        q = deque(new_q)

    return -1


n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
print(bfs())
