import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
MOD = 1000000007


def dfs(now, parent):
    global result
    dist = 1
    for node, d in graph[now]:
        if node == parent:
            continue

        dd = (dfs(node, now) * d) % MOD
        result += (dd * dist) % MOD
        result %= MOD
        dist += dd % MOD
        dist %= MOD

    return dist


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

result = 0
dfs(1, 0)
print(result)
