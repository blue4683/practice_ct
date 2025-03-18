from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9


def bfs():
    visited = [[INF] * 2 for _ in range(500001)]
    visited[n][0] = 0
    q = deque([(n, 0)])
    while q:
        x, t = q.popleft()
        for xx in [x + 1, x - 1, x * 2]:
            if xx < 0 or xx > 500000 or visited[xx][(t + 1) % 2] <= t + 1:
                continue

            visited[xx][(t + 1) % 2] = t + 1
            q.append((xx, t + 1))

    kk = k
    t = -1
    results = [INF, INF]
    while kk <= 500000:
        if INF not in results:
            break

        t += 1
        kk += t
        if kk > 500000:
            break

        if visited[kk][t % 2] > t:
            continue

        results[t % 2] = min(results[t % 2], t)

    result = min(results)
    return result if result != INF else -1


n, k = map(int, input().split())
print(bfs())
