import sys
input = sys.stdin.readline

d = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return 1

    return 0


def find_heart():
    for y in range(n):
        for x in range(n):
            if cookie[y][x] == '_':
                continue

            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or cookie[yy][xx] == '_':
                    break

            else:
                return y, x


def find_arms(y, x):
    left, right = 0, 0
    for xx in range(x - 1, -1, -1):
        if cookie[y][xx] != '*':
            break

        left += 1

    for xx in range(x + 1, n):
        if cookie[y][xx] != '*':
            break

        right += 1

    return [left, right]


def find_lower_body(y, x):
    waist = 0
    for yy in range(y + 1, n):
        if cookie[yy][x] != '*':
            break

        waist += 1

    left, right = find_legs(yy, x)

    return [waist, left, right]


def find_legs(y, x):
    left, right = 0, 0
    for yy in range(y, n):
        if cookie[yy][x - 1] != '*':
            break

        left += 1

    for yy in range(y, n):
        if cookie[yy][x + 1] != '*':
            break

        right += 1

    return left, right


def find_cookie():
    result = []

    y, x = find_heart()
    result += find_arms(y, x)
    result += find_lower_body(y, x)

    return y, x, result


n = int(input())
cookie = [list(input().rstrip()) for _ in range(n)]
y, x, result = find_cookie()
print(y + 1, x + 1)
print(*result)
