from collections import deque
import sys

input = sys.stdin.readline

d = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs(sy, sx, cnt):
    q = deque([(sy, sx)])
    pos = [(sy, sx)]
    result[sy][sx] = "-1"
    possible = -1

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if (
                0 <= yy < n
                and 0 <= xx < m
                and arr[yy][xx] == "0"
                and result[yy][xx][0] == "0"
            ):
                possible -= 1
                result[yy][xx][0] = "-1"
                pos.append((yy, xx))
                q.append((yy, xx))

    for y, x in pos:
        result[y][x] = [str(possible), cnt]


n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
pos = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == "0"]
target = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == "1"]
result = [[[arr[y][x], 0] for x in range(m)] for y in range(n)]

cnt = 0
for y, x in pos:
    if result[y][x][0] == "0":
        bfs(y, x, cnt)
        cnt += 1

for y, x in target:
    tmp = 1
    duplicated = []
    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if (
            0 <= yy < n
            and 0 <= xx < m
            and int(result[yy][xx][0]) < 0
            and result[yy][xx][1] not in duplicated
        ):
            tmp -= int(result[yy][xx][0])
            duplicated.append(result[yy][xx][1])
    arr[y][x] = str(tmp % 10)

for line in arr:
    print("".join(line))
