import sys

input = sys.stdin.readline


def seperate(arr, num):
    new_arr = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if num and (y + x) % 2 and arr[y][x] == 1:
                new_arr[y][x] = 1

            if not num and not (y + x) % 2 and arr[y][x] == 1:
                new_arr[y][x] = 1

    return new_arr


def check(pos, placed):
    y, x = pos
    for yy, xx in placed:
        if abs(yy - y) == abs(xx - x):
            return False

    return True


def dfs(y, x, plate, placed):
    global results
    if x == n and y == n - 1:
        results.append(len(placed))
        return

    if x == n:
        dfs(y + 1, 0, plate, placed)
        return

    if plate[y][x] and check((y, x), placed):
        plate[y][x] = 0
        placed.append((y, x))
        dfs(y, x + 1, plate, placed)
        placed.pop()
        plate[y][x] = 1

    dfs(y, x + 1, plate, placed)


n = int(input())
plate = [list(map(int, input().split())) for _ in range(n)]
black, white = seperate(plate, 0), seperate(plate, 1)

result = 0

for arr in [black, white]:
    results = []
    dfs(0, 0, arr, [])
    result += max(results)

print(result)
