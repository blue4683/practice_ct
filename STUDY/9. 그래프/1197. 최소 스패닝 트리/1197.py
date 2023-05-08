import sys
input=sys.stdin.readline

def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if a>b: graph[a]=b
    else: graph[b]=a

v,e=map(int,input().split())
edges=[list(map(int,input().split())) for _ in range(e)]
edges.sort(key=lambda x:x[-1])
graph=[i for i in range(v+1)]
answer=0
for now,next,cost in edges:
    if find(now)!=find(next):
        union(now,next)
        answer+=cost
print(answer)