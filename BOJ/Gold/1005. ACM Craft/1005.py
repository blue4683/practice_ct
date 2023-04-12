from collections import deque
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    cost=[0]+list(map(int,input().split()))
    graph=[[] for _ in range(n+1)]
    indegree=[0]*(n+1)
    result=[0]*(n+1)
    for _ in range(k):
        f,b=map(int,input().split())
        graph[f]+=[b]
        indegree[b]+=1
    w=int(input())
    target=graph[w]
    q=deque()
    
    for i in range(1,n+1):
        if not indegree[i]:
            result[i]+=cost[i]
            q+=[i]

    while indegree[w]>0:
        now=q.popleft()
        for i in graph[now]:
            indegree[i]-=1
            result[i]=max(result[i],cost[i]+result[now])
            if not indegree[i]:
                q+=[i]

    print(result[w])