import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(node, prev):
    global result
    value = 1
    for next_node in graph[node]:
        if prev == next_node:
            continue

        cnt = dfs(next_node, node)
        k = n - cnt
        result += cnt * k + cnt * (cnt - 1) // 2
        value += cnt

    return value


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
dfs(1, 1)
print(result)
