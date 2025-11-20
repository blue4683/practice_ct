import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    weight = weights[now]
    for node in graph[now]:
        w = dfs(node)
        if w > 0:
            weight += w

    return weight


n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = map(int, input().split())
    graph[p].append(c)

weights = list(map(int, input().split()))
print(dfs(0))
