from collections import deque
import sys
input=sys.stdin.readline

def topological_sort():
    q=deque([])
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now=q.popleft()
        for next,time in graph[now]:
            indegree[next]-=1
            result[next]=max(result[next],result[now]+time)
            if indegree[next]==0:
                q.append(next)
    
    q=deque([arrival])
    no_rest=0
    visited=[0]*(n+1)

    while q:
        now=q.popleft()
        for next,time in reverse_graph[now]:
            if result[next]+time==result[now]:
                no_rest+=1
                if visited[next]==0:
                    visited[next]=1
                    q.append(next)
    print(result[arrival])
    print(no_rest)

n=int(input())
m=int(input())
info=[list(map(int,input().split())) for _ in range(m)]
departure,arrival=map(int,input().split())
graph=[[] for _ in range(n+1)]
reverse_graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
result=[0]*(n+1)

for i in info:
    s,e,t=i
    graph[s].append([e,t])
    reverse_graph[e].append([s,t])
    indegree[e]+=1

topological_sort()