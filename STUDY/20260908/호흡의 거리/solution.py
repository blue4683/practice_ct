def dfs(now, parent, depth):
    global answer
    if now == v:
        answer = depth
        return

    for node in graph[now]:
        if node != parent:
            dfs(node, now, depth + 1)
            

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
u, v = map(int, input().split())
answer = 10 ** 9
dfs(u, -1, 0)

print(answer)
