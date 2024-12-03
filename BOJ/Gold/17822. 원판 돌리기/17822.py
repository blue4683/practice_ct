from collections import deque
import sys
input = sys.stdin.readline
d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def rotate(y, dir, k):
    if dir:
        for _ in range(k):
            circles[y].append(circles[y].popleft())

    else:
        for _ in range(k):
            circles[y].appendleft(circles[y].pop())


def delete_same_number():
    same_number = set()
    for y in range(n):
        for x in range(m):
            if not circles[y][x]:
                continue

            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if yy < 0 or yy > n - 1:
                    continue

                if xx == -1:
                    xx = m - 1

                if xx == m:
                    xx = 0

                if circles[y][x] == circles[yy][xx]:
                    same_number |= {(y, x), (yy, xx)}

    for y, x in same_number:
        circles[y][x] = 0

    if not same_number:
        total, cnt = 0, 0
        for y in range(n):
            for x in range(m):
                if not circles[y][x]:
                    continue

                total += circles[y][x]
                cnt += 1

        if not cnt:
            return

        mean = total / cnt
        for y in range(n):
            for x in range(m):
                if not circles[y][x]:
                    continue

                if mean > circles[y][x]:
                    circles[y][x] += 1

                elif mean < circles[y][x]:
                    circles[y][x] -= 1


n, m, t = map(int, input().split())
circles = [deque(map(int, input().split())) for _ in range(n)]

for _ in range(t):
    x, dir, k = map(int, input().split())
    for y in range(1, n + 1):
        if y % x:
            continue

        rotate(y - 1, dir, k)

    delete_same_number()

print(sum(map(sum, circles)))
