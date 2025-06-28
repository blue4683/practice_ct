import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def set_seat(num):
    possible = []
    for y in range(n):
        for x in range(n):
            if arr[y][x]:
                continue

            blank, friend = 0, 0
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx):
                    continue

                if not arr[yy][xx]:
                    blank += 1

                elif arr[yy][xx] in students[num]:
                    friend += 1

            possible.append((-friend, -blank, y, x))

    possible.sort()
    return possible[0][2:]


n = int(input())
arr = [[0] * n for _ in range(n)]
students = {}
for _ in range(n ** 2):
    i, *nums = map(int, input().split())
    students[i] = set(nums)
    y, x = set_seat(i)
    arr[y][x] = i

result = 0
for y in range(n):
    for x in range(n):
        friend = 0
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            if arr[yy][xx] in students[arr[y][x]]:
                friend += 1

        result += 10 ** (friend - 1) if friend else 0

print(result)
