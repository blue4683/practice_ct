from collections import deque
import sys
input=sys.stdin.readline

def dfs(v):
    print(v,end=' ')
    for node in graph[v]:
        if not visited[node]:
            visited[node]=1
            dfs(node)

def bfs(v):
    q=deque([v])
    while q:
        node=q.popleft()
        print(node,end=' ')
        for i in graph[node]:
            if not visited[i]:
                visited[i]=1
                q.append(i)

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e=map(int,input().split())
    graph[s]+=[e]
    graph[e]+=[s]
graph=list(map(sorted,graph))
for i in range(2):
    visited=[0]*(n+1)
    visited[v]=1
    dfs(v) if not i else bfs(v)
    print()