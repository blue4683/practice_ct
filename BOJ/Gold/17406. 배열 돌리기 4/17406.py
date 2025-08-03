from itertools import permutations
import sys
input = sys.stdin.readline


def rotate(arr, r, c, s):
    y1, y2, x1, x2 = r - s - 1, r + s - 1, c - s - 1, c + s - 1
    while y1 != y2 and x1 != x2:
        top, bottom = arr[y1][x1:x2], arr[y2][x2:x1:-1]
        left, right = [arr[i][x1] for i in range(
            y2, y1, -1)], [arr[i][x2] for i in range(y1, y2)]
        for i in range(1, len(top) + 1):
            arr[y1][x1 + i] = top[i - 1]
            arr[y1 + i][x2] = right[i - 1]
            arr[y2][x2 - i] = bottom[i - 1]
            arr[y2 - i][x1] = left[i - 1]

        y1 += 1
        x1 += 1
        y2 -= 1
        x2 -= 1

    return arr


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
operations = [list(map(int, input().split())) for _ in range(k)]
orders = permutations(range(k))
result = 10 ** 9
for order in orders:
    new_arr = [l[:] for l in arr]
    for i in order:
        new_arr = rotate(new_arr, *operations[i])

    result = min(result, min(map(sum, new_arr)))

print(result)
