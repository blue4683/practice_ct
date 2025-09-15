from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([arr])
    visited = defaultdict(int)
    visited[tuple(arr)] = 1
    while q:
        x = q.popleft()
        if x == result:
            return visited[tuple(x)] - 1

        for i in range(n - k + 1):
            xx = x[:i] + x[i:i + k][::-1] + x[i + k:]
            if visited[tuple(xx)]:
                continue

            visited[tuple(xx)] = visited[tuple(x)] + 1
            q.append(xx)

    return -1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = sorted(arr)
print(bfs())
