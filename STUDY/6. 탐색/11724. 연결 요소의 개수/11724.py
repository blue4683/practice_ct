import sys
input=sys.stdin.readline

def find(x):
    if x!=graph[x]:
        return find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if b>a:
        graph[b]=a
    else:
        graph[a]=b

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
graph=[0]*(n+1)
cnt=n
for i in range(1,n+1):
    graph[i]=i
for s,e in arr:
    if find(s)!=find(e):
        cnt-=1
        union(s,e)
print(cnt)