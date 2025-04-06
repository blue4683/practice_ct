from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [0] * 101
    visited[1] = 1
    q = deque([1])
    while q:
        x = q.popleft()
        if x == 100:
            return visited[x] - 1

        for dx in range(1, 7):
            if x + dx > 100:
                continue

            xx = arr[x + dx]
            if visited[xx]:
                continue

            visited[xx] = visited[x] + 1
            q.append(xx)

    return -1


n, m = map(int, input().split())
arr = [i for i in range(101)]
for x, y in [map(int, input().split()) for _ in range(n + m)]:
    arr[x] = y

print(bfs())
