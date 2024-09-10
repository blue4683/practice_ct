import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cctv_dir = {1: [0], 2: [0, 2], 3: [0, 3], 4: [0, 2, 3], 5: [0, 1, 2, 3]}
cnts = {1: 4, 2: 2, 3: 4, 4: 4, 5: 1}


def check(arr):
    cnt = 0
    for y in range(n):
        for x in range(m):
            if not arr[y][x]:
                cnt += 1

    return cnt


def dfs(depth, arr):
    global result
    if depth == len(pos):
        result = min(result, check(arr))
        return

    y, x = pos[depth]
    cctv = arr[y][x]
    for i in range(cnts[cctv]):
        detected = []
        for dy, dx in map(lambda x: d[(x + i) % 4], cctv_dir[cctv]):
            k = 1
            while 0 <= y + k * dy < n and 0 <= x + k * dx < m and arr[y + k * dy][x + k * dx] != 6:
                if not arr[y + k * dy][x + k * dx]:
                    detected.append((y + k * dy, x + k * dx))

                k += 1

        for yy, xx in detected:
            arr[yy][xx] = '#'

        dfs(depth + 1, arr)

        for yy, xx in detected:
            arr[yy][xx] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = [(y, x) for y in range(n) for x in range(m) if 1 <= arr[y][x] < 6]
result = n * m
dfs(0, arr)

print(result)
