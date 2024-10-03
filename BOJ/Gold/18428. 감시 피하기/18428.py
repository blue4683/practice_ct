import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def is_blocked(arr):
    teachers = [(y, x) for y in range(n) for x in range(n) if arr[y][x] == 'T']
    for y, x in teachers:
        for dy, dx in d:
            k = 1
            while not out_of_range(y + dy * k, x + dx * k):
                if arr[y + dy * k][x + dx * k] == 'S':
                    return 0

                if arr[y + dy * k][x + dx * k] == 'O':
                    break

                k += 1

    return 1


def set_up_obstacles(cnt, arr):
    global result
    if result == 'YES':
        return

    if cnt == 3:
        if is_blocked(arr):
            result = 'YES'

        return

    for y in range(n):
        for x in range(n):
            if arr[y][x] != 'X':
                continue

            arr[y][x] = 'O'
            set_up_obstacles(cnt + 1, arr)
            arr[y][x] = 'X'


n = int(input())
arr = [input().split() for _ in range(n)]
result = 'NO'
set_up_obstacles(0, arr)

print(result)
