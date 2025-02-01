from collections import deque
import sys
input = sys.stdin.readline
d = [-1, 1, 2]


def get_path():
    arr = deque()
    now = k
    for _ in range(dist[k] + 1):
        arr.appendleft(now)
        now = visited[now]

    return arr


def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            print(dist[now])
            print(*get_path())
            return

        for nxt in [now + 1, now - 1, 2 * now]:
            if nxt < 0 or nxt > 10 ** 5 or dist[nxt]:
                continue

            dist[nxt] = dist[now] + 1
            visited[nxt] = now
            q.append(nxt)


n, k = map(int, input().split())
dist = [0] * (10 ** 5 + 1)
visited = [0] * (10 ** 5 + 1)

bfs()
