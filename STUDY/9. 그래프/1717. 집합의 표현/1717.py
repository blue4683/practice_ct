import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def find(x):
    if x!=graph[x]:
        graph[x]=find(graph[x])
    return graph[x]

def union(a,b):
    a,b=find(a),find(b)
    if a==b: return
    if a>b: graph[a]=b
    else: graph[b]=a

def check(a,b):
    if find(a)==find(b):
        return 'YES'
    return 'NO'

n,m=map(int,input().split())
graph=[i for i in range(n+1)]
for _ in range(m):
    o,a,b=map(int,input().split())
    if o: print(check(a,b))
    else: union(a,b)