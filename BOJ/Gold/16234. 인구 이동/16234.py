from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(sy, sx, num, visited, cnt, migration):
    q = deque([(sy, sx)])
    visited[sy][sx] = num
    cnt[num] += 1
    migration[num] += population[sy][sx]

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if 0 <= yy < n and 0 <= xx < n and not visited[yy][xx]:
                if l <= abs(population[yy][xx] - population[y][x]) <= r:
                    visited[yy][xx] = num
                    cnt[num] += 1
                    migration[num] += population[yy][xx]
                    q.append((yy, xx))

    return visited, cnt, migration


def migrate():
    global population

    visited = [[0] * n for _ in range(n)]
    cnt = [0] * 2
    migration = [0] * 2
    num = 1

    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                continue

            visited, cnt, migration = bfs(y, x, num, visited, cnt, migration)
            num += 1
            cnt.append(0)
            migration.append(0)

    if set(cnt) == {0, 1}:
        return 0

    migration = [0] + \
        list(map(lambda x, y: x // y, migration[1:-1], cnt[1:-1]))
    for y in range(n):
        for x in range(n):
            if visited[y][x]:
                population[y][x] = migration[visited[y][x]]

    return 1


n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
result = 0

while migrate():
    result += 1

print(result)
