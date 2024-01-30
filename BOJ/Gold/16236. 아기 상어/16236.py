from collections import deque
import sys
input = sys.stdin.readline

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def eat(sy, sx):
    global ate, size
    visited = [[0] * n for _ in range(n)]
    visited[sy][sx] = 1
    q = deque([(sy, sx)])
    possible = []

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx]:
                if space[yy][xx] in [0, size]:
                    visited[yy][xx] = visited[y][x] + 1
                    q.append((yy, xx))

                elif space[yy][xx] < size:
                    possible.append((visited[y][x], yy, xx))

                elif space[yy][xx] > size:
                    visited[yy][xx] = 999

    if possible:
        possible.sort()
        ate += 1
        if ate == size:
            size += 1
            ate = 0

        return possible[0]

    return (0, 0, 0)


n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
start = [(y, x) for y in range(n) for x in range(n) if space[y][x] == 9][0]
cnt = n ** 2 + 1
ate = 0
size = 2
result = 0

while cnt:
    cnt -= 1
    next = eat(*start)
    if next == (0, 0, 0):
        break

    else:
        result += next[0]
        space[start[0]][start[1]] = 0
        space[next[1]][next[2]] = 9
        start = next[1:]

print(result)
