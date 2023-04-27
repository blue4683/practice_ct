from collections import deque
import sys
input=sys.stdin.readline

def topological_sort():
    result=[]
    q=deque()

    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)
    
    while q:
        now=q.popleft()
        result+=[now]
        for i in graph[now]:
            indegree[i]-=1
            if not indegree[i]:
                q.append(i)      
    print(*result)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)
for _ in range(m):
    f,b=map(int,input().split())
    graph[f]+=[b]
    indegree[b]+=1
topological_sort()