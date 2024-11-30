from collections import Counter
import sys
input = sys.stdin.readline


def cal_r(row, col):
    max_col = 0
    for y in range(row):
        counter = Counter(arr[y])
        if counter == Counter([0] * 100):
            return row, max_col

        tmp = [0] * 100
        x = 0
        for value, cnt in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            if not value:
                continue

            tmp[x], tmp[x + 1] = value, cnt
            x += 2
            max_col = max(max_col, x)
            if x == 100:
                break

        for i in range(100):
            arr[y][i] = tmp[i]

    return row, max_col


def cal_c(row, col):
    max_row = 0
    for x in range(col):
        counter = Counter([arr[y][x] for y in range(100)])
        if counter == Counter([0] * 100):
            return max_row, col

        tmp = [0] * 100
        y = 0
        for value, cnt in sorted(counter.items(), key=lambda x: (x[1], x[0])):
            if not value:
                continue

            tmp[y], tmp[y + 1] = value, cnt
            y += 2
            max_row = max(max_row, y)
            if y == 100:
                break

        for i in range(100):
            arr[i][x] = tmp[i]

    return max_row, col


r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for y in range(3):
    x = 0
    for v in map(int, input().split()):
        arr[y][x] = v
        x += 1

row, col = 3, 3
result = -1
for i in range(101):
    if arr[r - 1][c - 1] == k:
        result = i
        break

    if row >= col:
        row, col = cal_r(row, col)

    else:
        row, col = cal_c(row, col)

print(result)
