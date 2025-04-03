from collections import deque
import sys
input = sys.stdin.readline


def get_dist(y, x, yy, xx):
    return abs(y - yy) + abs(x - xx)


def bfs():
    visited = [0] * n
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        if get_dist(y, x, ey, ex) <= 1000:
            return 'happy'

        for i in range(n):
            if visited[i] or get_dist(y, x, *stores[i]) > 1000:
                continue

            visited[i] = 1
            q.append(stores[i])

    return 'sad'


for _ in range(int(input())):
    n = int(input())
    sy, sx = map(int, input().split())
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    ey, ex = map(int, input().split())
    print(bfs())
