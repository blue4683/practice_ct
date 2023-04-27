import sys
input=sys.stdin.readline

def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if a==b: return
    graph[b]=a

n,m=map(int,input().split())
truth=list(map(int,input().split()))
parties=[list(map(int,input().split())) for _ in range(m)]
graph=[i for i in range(n+1)]
result=0
if truth==[0]: result=m
else:
    for party in parties:
        for p in party[2:]:
            union(party[1],p)
    for party in parties:
        for known in truth[1:]:
            if find(party[1])==find(known):
                break
        else:
            result+=1
print(result)