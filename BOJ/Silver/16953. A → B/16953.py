from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs():
    visited = defaultdict(int)
    visited[a] = 1
    q = deque([a])
    while q:
        x = q.popleft()
        if x == b:
            return visited[x]

        if x * 2 <= b and not visited[x * 2]:
            visited[x * 2] = visited[x] + 1
            q.append(x * 2)

        xx = int(str(x) + '1')
        if xx <= b and not visited[xx]:
            visited[xx] = visited[x] + 1
            q.append(xx)

    return -1


a, b = map(int, input().split())
print(bfs())
