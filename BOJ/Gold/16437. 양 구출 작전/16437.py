import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(node):
    s = weights[node]
    for next in graph[node]:
        s += dfs(next)

    if s < 0:
        return 0

    else:
        return s


n = int(input())
graph = [[] for _ in range(n + 1)]
weights = [0] * (n + 1)

for i in range(2, n + 1):
    t, a, p = input().rstrip().split()
    weights[i] = int(a) if t == 'S' else -int(a)
    graph[int(p)].append(i)

print(dfs(1))
