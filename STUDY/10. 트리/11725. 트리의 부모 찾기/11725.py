import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(now,pre):
    if now!=1: result[now]=pre
    for next in graph[now]:
        if visited[next]==0:
            visited[next]=1
            dfs(next,now)

n=int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
result=[0]*(n+1)
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited[1]=1
dfs(1,0)
print(*result[2:])