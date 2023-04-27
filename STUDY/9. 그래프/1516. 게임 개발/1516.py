from collections import deque
import sys
input=sys.stdin.readline

def topological_sort():
    q=deque([])
    for i in range(1,n+1):
        if indegree[i]==0:
            result[i]=cost[i]
            q.append(i)
    
    while q:
        now=q.popleft()
        for node in graph[now]:
            indegree[node]-=1
            result[node]=max(result[node],result[now]+cost[node])
            if indegree[node]==0:
                q.append(node)
    for res in result[1:]:
        print(res)

n=int(input())
graph=[[] for _ in range(n+1)]
cost=[0]*(n+1)
result=[0]*(n+1)
indegree=[0]*(n+1)
for i in range(1,n+1):
    info=list(map(int,input().split()))
    cost[i]=info[0]
    if len(info)==2:
        continue
    for node in info[1:-1]:
        graph[node].append(i)
        indegree[i]+=1
topological_sort()