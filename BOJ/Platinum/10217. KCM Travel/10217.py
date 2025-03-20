from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9


def bfs():
    result = INF
    q = deque([(1, 0)])
    while q:
        x, c = q.popleft()
        for xx, cc, tt in graph[x]:
            if c + cc > m or dp[xx][c + cc] <= dp[x][c] + tt or dp[x][c] + tt >= result:
                continue

            dp[xx][c + cc] = dp[x][c] + tt
            if xx == n:
                result = min(result, dp[xx][c + cc])
                break

            for i in range(c + cc + 1, m + 1):
                if dp[xx][i] <= dp[xx][c + cc]:
                    break

                dp[xx][i] = dp[xx][c + cc]

            q.append((xx, c + cc))

    return result if result != INF else 'Poor KCM'


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for u, v, c, d in sorted([list(map(int, input().split())) for _ in range(k)], key=lambda x: (x[-1], x[-2])):
        graph[u].append((v, c, d))

    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    dp[1][0] = 0
    print(bfs())
