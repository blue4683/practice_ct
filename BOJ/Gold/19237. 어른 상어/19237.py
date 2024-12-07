from collections import defaultdict
import sys
input = sys.stdin.readline
d = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


n, m, k = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(n)]
shark = [0] + list(map(int, input().split()))
directions = [[]]
for i in range(m):
    direction = [[]] + [[0] + list(map(int, input().split()))
                        for _ in range(4)]
    directions.append(direction)

arr = defaultdict(list)
sharks = []
for y in range(n):
    for x in range(n):
        if not tmp[y][x]:
            continue

        arr[(y, x)] = [tmp[y][x], shark[tmp[y][x]], k]
        sharks.append(((y, x), [tmp[y][x], shark[tmp[y][x]], k]))

result = -1
for time in range(1001):
    if len(sharks) == 1:
        result = time
        break

    if time == 1000:
        break

    moved_sharks = []
    for (y, x), (shark, dir, _) in sharks:
        for i in directions[shark][dir]:
            if not i:
                continue

            dy, dx = d[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[(yy, xx)]:
                continue

            moved_sharks.append(((yy, xx), [shark, i, k]))
            break

        else:
            for i in directions[shark][dir]:
                if not i:
                    continue

                dy, dx = d[i]
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or arr[(yy, xx)][0] != shark:
                    continue
                moved_sharks.append(((yy, xx), [shark, i, k]))
                break

    keys = list(arr.keys())[:]
    for key in keys:
        if not arr[key] or arr[key][-1] == 1:
            del arr[key]

        else:
            arr[key][-1] -= 1

    sharks = []
    moved_sharks.sort(key=lambda x: x[1][0])
    for key, value in moved_sharks:
        if arr[key] and arr[key][0] != value[0]:
            continue

        arr[key] = value
        sharks.append((key, value))

print(result)
