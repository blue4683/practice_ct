from collections import deque
import sys
input=sys.stdin.readline

def bfs(x):
    q=deque([x])
    visited=[0]*(n+1)
    visited[x]=1
    while q:
        now=q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node]=1
                connection[node]+=1
                q.append(node)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
connection=[0]*(n+1)
for _ in range(m):
    s,e=map(int,input().split())
    graph[s].append(e)

for i in range(1,n+1):
    bfs(i)

max_connection=0
for i in range(1,n+1):
    max_connection=max(max_connection,connection[i])
    
for i in range(1,n+1):
    if connection[i]==max_connection:
        print(i,end=' ')