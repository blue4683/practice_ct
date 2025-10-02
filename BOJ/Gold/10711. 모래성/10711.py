from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def out_of_range(y, x):
    if y < 0 or y >= h or x < 0 or x >= w:
        return 1

    return 0


h, w = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]

q = deque()
for y in range(h):
    for x in range(w):
        if arr[y][x] == '.':
            arr[y][x] = 0
            q.append((y, x))

        else:
            arr[y][x] = int(arr[y][x])

cnt = 0
while 1:
    new_q = set()
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if not out_of_range(yy, xx) and arr[yy][xx] != '.':
                arr[yy][xx] -= 1
                if not arr[yy][xx]:
                    new_q.add((yy, xx))

    if not new_q:
        break

    q = deque(new_q)
    cnt += 1

print(cnt)
