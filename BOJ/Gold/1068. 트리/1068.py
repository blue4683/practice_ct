import sys
input = sys.stdin.readline


def dfs(node):
    global result
    if not graph[node] or graph[node] == [exception]:
        result += 1
        return

    for next in graph[node]:
        if next == exception:
            continue

        dfs(next)


n = int(input())
nodes = list(map(int, input().split()))
graph = [[] for _ in range(n)]
root = 0
for i in range(n):
    if nodes[i] == -1:
        root = i
        continue

    graph[nodes[i]].append(i)

exception = int(input())
result = 0
if root != exception:
    dfs(root)

print(result)
