from collections import deque
import sys
input=sys.stdin.readline

def bfs(start):
    visited[start]=0
    q=deque([start])
    while q:
        now=q.popleft()
        for node in graph[now]:
            if visited[node]>visited[now]+1:
                visited[node]=visited[now]+1
                q+=[node]

N,M,K,X=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited=[1e9]*(N+1)
result=[]
for _ in range(M):
    s,e=map(int,input().split())
    graph[s]+=[e]
bfs(X)
for i in range(N+1):
    if visited[i]==K:
        result+=[i]
if not result:
    print(-1)
else:
    for node in sorted(result):
        print(node)