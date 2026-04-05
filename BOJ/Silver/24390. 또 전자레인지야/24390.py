from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9


def bfs():
    q = deque([(0, 0)])
    visited = [[INF] * 2 for _ in range(t + 1)]
    visited[0][0] = 0
    while q:
        x, cooking = q.popleft()
        if not cooking:
            if not x:
                if t >= 3:
                    visited[3][1] = 1
                    q.append((3, 1))

            else:
                if visited[x][1] > visited[x][cooking] + 1:
                    visited[x][1] = visited[x][cooking] + 1
                    q.append((x, 1))

        else:
            if x + 3 <= t and visited[x + 3][cooking] > visited[x][cooking] + 1:
                visited[x + 3][cooking] = visited[x][cooking] + 1
                q.append((x + 3, cooking))

        for dx in [1, 6, 60]:
            xx = x + dx
            if xx > t or visited[xx][cooking] <= visited[x][cooking] + 1:
                continue

            visited[xx][cooking] = visited[x][cooking] + 1
            q.append((xx, cooking))

    return visited[t][1]


m, s = map(int, input().split(':'))
t = (m * 60 + s) // 10
if t == 3:
    print(1)

else:
    print(bfs())
