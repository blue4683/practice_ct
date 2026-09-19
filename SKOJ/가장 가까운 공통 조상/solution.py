import sys
sys.setrecursionlimit(10 ** 6)


def dfs(depth, now, before):
    levels[now] = depth
    if before != -1:
        parents[now] = before
    
    for node in graph[now]:
        if levels[node] == -1:
            dfs(depth + 1, node, now)


n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parents = [i for i in range(n + 1)]    
levels = [-1] * (n + 1)
dfs(0, 1, -1)

a, b = map(int, input().split())
la, lb = levels[a], levels[b]
if la > lb:
    for _ in range(la - lb):
        a = parents[a]

else:
    for _ in range(lb - la):
        b = parents[b]
      
while a != b:
    a, b = parents[a], parents[b]
    
print(a)
