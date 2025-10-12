from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(k):
    visited = defaultdict(int)
    for x in arr:
        visited[x] = 1

    q = deque(arr)
    while 1:
        x = q.popleft()
        for dx in [-1, 1]:
            xx = x + dx
            if visited[xx]:
                continue

            k -= 1
            visited[xx] = visited[x] + 1
            if not k:
                result = visited.values()
                return sum(result) - len(result)

            q.append(xx)


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(bfs(k))
