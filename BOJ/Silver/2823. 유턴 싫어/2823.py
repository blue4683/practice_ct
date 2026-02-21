import sys
input = sys.stdin.readline
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= r or x < 0 or x >= c:
        return 1

    return 0


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
for y in range(r):
    for x in range(c):
        if arr[y][x] == '.':
            cnt = 0
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or arr[yy][xx] == 'X':
                    continue

                cnt += 1

            if cnt <= 1:
                print(1)
                exit()

print(0)
