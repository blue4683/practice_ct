import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now, before):
    result[now] = appreciate[now] + result[before]
    for next in graph[now]:
        dfs(next, now)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(1, n):
    graph[arr[i]].append(i + 1)

appreciate = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    appreciate[a] += b

result = [0] * (n + 1)
dfs(1, 0)
print(*result[1:])
