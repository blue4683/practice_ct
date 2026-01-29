from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9


def calculate(a, b, mod):
    if mod == '+':
        return a + b

    if mod == '-':
        return a - b

    return a * b


def out_of_range(y, x):
    if y >= n or x >= n:
        return 1

    return 0


def bfs():
    q = deque([(0, 0, '')])
    for i in range(2):
        visited[0][0][i] = int(arr[0][0])

    while q:
        y, x, mod = q.popleft()
        for dy, dx in [(0, 1), (1, 0)]:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx):
                continue

            if mod == '':
                flag = 0
                if visited[yy][xx][0] == INF or visited[y][x][0] > visited[yy][xx][0]:
                    visited[yy][xx][0] = visited[y][x][0]
                    flag = 1

                if visited[yy][xx][1] == -INF or visited[y][x][1] < visited[yy][xx][1]:
                    visited[yy][xx][1] = visited[y][x][1]
                    flag = 1

                if flag:
                    q.append((yy, xx, arr[yy][xx]))

            else:
                max_v = max(calculate(visited[y][x][0], int(arr[yy][xx]), mod), calculate(
                    visited[y][x][1], int(arr[yy][xx]), mod))
                min_v = min(calculate(visited[y][x][0], int(arr[yy][xx]), mod), calculate(
                    visited[y][x][1], int(arr[yy][xx]), mod))
                flag = 0
                if max_v > visited[yy][xx][0]:
                    visited[yy][xx][0] = max_v
                    flag = 1

                if min_v < visited[yy][xx][1]:
                    visited[yy][xx][1] = min_v
                    flag = 1

                if flag:
                    q.append((yy, xx, ''))

    return visited[n - 1][n - 1]


n = int(input())
arr = [input().split() for _ in range(n)]
visited = [[[-INF, INF] for _ in range(n)] for _ in range(n)]
print(*bfs())
