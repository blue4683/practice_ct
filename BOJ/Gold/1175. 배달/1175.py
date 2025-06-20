from collections import deque
import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return 1

    return 0


def bfs():
    q = deque([(*start, i, 0) for i in range(4)])
    visited = [[[[0] * 4 for _ in range(1 << 2)]
                for _ in range(m)] for _ in range(n)]
    while q:
        y, x, direction, visited_dest = q.popleft()
        if visited_dest == 3:
            return visited[y][x][visited_dest][direction]

        for i in range(4):
            if direction == i:
                continue

            dy, dx = d[i]
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or arr[yy][xx] == '#' or visited[yy][xx][visited_dest][i]:
                continue

            if arr[yy][xx] == 'C':
                visited[yy][xx][visited_dest | 1 << idx[(
                    yy, xx)]][i] = visited[y][x][visited_dest][direction] + 1
                q.append((yy, xx, i, visited_dest | 1 << idx[(yy, xx)]))

            else:
                visited[yy][xx][visited_dest][i] = visited[y][x][visited_dest][direction] + 1
                q.append((yy, xx, i, visited_dest))

    return -1


n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

start = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'S'][0]
dests = [(y, x) for y in range(n) for x in range(m) if arr[y][x] == 'C']
idx = {dests[i]: i for i in range(2)}
print(bfs())
