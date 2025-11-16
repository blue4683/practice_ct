import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(now):
    if depth[nums[k]] != -1:
        return

    for node in graph[now]:
        depth[node] = depth[now] + 1
        dfs(node)


n, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c = map(int, input().split())
    graph[p].append(c)

nums = [i for i in range(n + 1)]
for i, num in enumerate(map(int, input().split())):
    nums[num] = i

depth = [-1] * (n + 1)
depth[0] = 0
dfs(0)
print(depth[nums[k]])
