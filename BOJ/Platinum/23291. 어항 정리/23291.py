import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x, n, m):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def put_the_fish_in(arr):
    minv = min(arr)
    for i in range(n):
        if arr[i] == minv:
            arr[i] += 1

    return arr


def rotate_90(arr):
    n, m = len(arr), len(arr[0])
    new_arr = [[0] * n for _ in range(m)]
    for y in range(n):
        for x in range(m):
            new_arr[x][n - 1 - y] = arr[y][x]

    return new_arr


def rotate_180(arr):
    n, m = len(arr), len(arr[0])
    new_arr = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            new_arr[n - 1 - y][m - 1 - x] = arr[y][x]

    return new_arr


def line_up(arr):
    new_arr = []
    n, m = len(arr), len(arr[0])
    for x in range(m):
        for y in range(n - 1, -1, -1):
            if not arr[y][x]:
                continue

            new_arr.append(arr[y][x])

    return new_arr


def stack_bowl_gradually(arr):
    new_arr = [[arr[0]] + ([0] * (n - 2)), arr[1:]]
    while 1:
        m = len(new_arr[0])
        rn = len(new_arr)
        rm = 0
        for i in range(m):
            if not new_arr[0][i]:
                rm = i
                break

        else:
            rm = m

        if rn > m - rm:
            return new_arr

        tmp = [[0] * rm for _ in range(rn)]
        for y in range(rn):
            for x in range(rm):
                tmp[y][x] = new_arr[y][x]

        tmp = rotate_90(tmp)
        stacked_arr = []
        for l in tmp:
            stacked_arr.append(l[:] + ([0] * (m - rm - rn)))

        stacked_arr.append(new_arr[-1][rm:])
        new_arr = [l[:] for l in stacked_arr]


def stack_bowl_half(arr):
    n = len(arr)
    new_arr = [arr[:n // 2][::-1], arr[n // 2:]]
    n //= 2
    tmp = [[0] * (n // 2) for _ in range(2)]
    for y in range(2):
        for x in range(n // 2):
            tmp[y][x] = new_arr[y][x]

    tmp = rotate_180(tmp)
    stacked_arr = []
    for l in tmp:
        stacked_arr.append(l)

    for y in range(2):
        stacked_arr.append(new_arr[y][n // 2:])

    return stacked_arr[:]


def control_the_fish(arr):
    n, m = len(arr), len(arr[0])
    controlled = [[0] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if not arr[y][x]:
                continue

            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx, n, m) or arr[yy][xx] >= arr[y][x] or not arr[yy][xx]:
                    continue

                diff = (arr[y][x] - arr[yy][xx]) // 5
                controlled[yy][xx] += diff
                controlled[y][x] -= diff

    for y in range(n):
        for x in range(m):
            arr[y][x] += controlled[y][x]

    return arr


def check_min_max_diff(arr):
    minv, maxv = 10 ** 9, 0
    for fish in arr:
        if minv > fish:
            minv = fish

        if maxv < fish:
            maxv = fish

    return maxv - minv


n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
while check_min_max_diff(arr) > k:
    arr = put_the_fish_in(arr)
    arr = stack_bowl_gradually(arr)
    arr = control_the_fish(arr)
    arr = line_up(arr)
    arr = stack_bowl_half(arr)
    arr = control_the_fish(arr)
    arr = line_up(arr)
    result += 1

print(result)
