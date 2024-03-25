import sys
input = sys.stdin.readline


r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
result = ''

if r & (1 << 0):
    result = ('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * \
        (r // 2) + 'R' * (c - 1)

elif c & (1 << 0):
    result = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * \
        (c // 2) + 'D' * (r - 1)

else:
    low = 1000
    position = [-1, -1]

    for y in range(r):
        if y & (1 << 0) == 0:
            for x in range(1, c, 2):
                if low <= graph[y][x]:
                    continue

                low = graph[y][x]
                position = [y, x]

        else:
            for x in range(0, c, 2):
                if low <= graph[y][x]:
                    continue

                low = graph[y][x]
                position = [y, x]

    result = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    xx = x + 1

    while x != xx or y != r - 1:
        if x < xx and [y, xx] != position:
            x += 1
            result += 'R'

        elif x == xx and [y, xx - 1] != position:
            x -= 1
            result += 'L'

        if y != r - 1:
            y += 1
            result += 'D'

    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * \
        ((c - position[1] - 1) // 2)

print(result)
