from collections import defaultdict, deque
import sys
input = sys.stdin.readline


l, n, k = map(int, input().split())
light = set(map(int, input().split()))
q = deque(light)
visited = defaultdict(int)

for _ in range(k):
    x = q.popleft()
    print(visited[x])
    for dx in [-1, 1]:
        xx = x + dx
        if xx < 0 or xx > l or visited[xx] or xx in light:
            continue

        visited[xx] = visited[x] + 1
        q.append(xx)
