from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    visited = [0] * n
    visited[0] = 1
    q = deque([0])
    while q:
        x = q.popleft()
        if x == n - 1:
            return visited[x] - 1

        for dx in range(1, arr[x] + 1):
            xx = x + dx
            if xx >= n or visited[xx]:
                continue

            visited[xx] = visited[x] + 1
            q.append(xx)

    return -1


n = int(input())
arr = list(map(int, input().split()))
print(bfs())
