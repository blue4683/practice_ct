import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def connect(y, x):
    global place, result
    place[y][x] = 'x'

    if x == c - 1:
        result += 1
        return True

    if y - 1 >= 0 and place[y - 1][x + 1] != 'x':
        if connect(y - 1, x + 1):
            return True

    if place[y][x + 1] != 'x':
        if connect(y, x + 1):
            return True

    if y + 1 < r and place[y + 1][x + 1] != 'x':
        if connect(y + 1, x + 1):
            return True

    return False


r, c = map(int, input().split())
place = [list(input().rstrip()) for _ in range(r)]
result = 0

for y in range(r):
    connect(y, 0)

print(result)
