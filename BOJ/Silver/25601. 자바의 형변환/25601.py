from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(a, b):
    q = deque([a, b])
    while q:
        x = q.popleft()
        for xx in graph[x]:
            if xx in {a, b}:
                return 1

            q.append(xx)

    return 0


n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = input().split()
    graph[a].append(b)

a, b = input().split()
print(bfs(a, b))
