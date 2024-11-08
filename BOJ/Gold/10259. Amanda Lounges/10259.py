from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
INF = 10 ** 9


def dfs(node, visited):
    result = 0
    for airport, lounge in graph[node]:
        if visited[airport] == -1:
            if lounge == 0:
                if visited[node] == 1:
                    visited[airport] = 0
                    dfs(airport, visited)
                    result = INF

                else:
                    visited[airport] = 0
                    result += dfs(airport, visited)
                    result = min(result, INF)

            elif lounge == 1:
                if visited[node] == 1:
                    visited[airport] = 0
                    result += dfs(airport, visited)
                    result = min(result, INF)

                else:
                    visited[airport] = 1
                    result += 1
                    result += dfs(airport, visited)
                    result = min(result, INF)

            elif lounge == 2:
                if visited[node] == 0:
                    visited[airport] = 0
                    dfs(airport, visited)
                    result = INF

                else:
                    visited[airport] = 1
                    result += 1
                    result += dfs(airport, visited)
                    result = min(result, INF)

        else:
            if visited[node] + visited[airport] != lounge:
                result = INF

    return result


n, m = map(int, input().split())
graph = defaultdict(list)
visited1 = [-1] * (n + 1)
visited2 = [-1] * (n + 1)
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n + 1):
    if visited1[i] == -1:
        visited1[i] = 1
        res1 = dfs(i, visited1) + 1

        visited2[i] = 0
        res2 = dfs(i, visited2)

        ans += min(res1, res2)
        if ans > INF:
            ans = INF

if ans >= INF:
    print("impossible")

else:
    print(ans)
