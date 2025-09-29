from collections import deque
import sys
input = sys.stdin.readline


def out_of_range(x):
    if x < 0 or x >= n:
        return 1

    return 0


def bfs():
    q = deque([s])
    visited = [0] * n
    visited[s] = 1
    while q:
        x = q.popleft()
        for dx in [arr[x], -arr[x]]:
            xx = x + dx
            if out_of_range(xx) or visited[xx]:
                continue

            visited[xx] = 1
            q.append(xx)

    return sum(visited)


n = int(input())
arr = list(map(int, input().split()))
s = int(input()) - 1
print(bfs())
